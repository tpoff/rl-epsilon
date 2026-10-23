"""Convert ViZDoom .lmp demos from a training run into .mp4 videos, while the notebook is still running.

Usage:
    python lmp_to_mp4.py                       # every demo from the latest finished generation of the latest run
    python lmp_to_mp4.py --gen 12              # a specific generation of the latest run
    python lmp_to_mp4.py --run run-20261021_123226 --gen 12
    python lmp_to_mp4.py path/to/demo.lmp ...  # specific demos

Each .mp4 is written next to its .lmp. Videos are silent, since audio capture is silent on macOS anyway.
"""

import argparse
import re
import shutil
import tempfile
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
import vizdoom as vzd

EXPERIMENT_DIR = Path(__file__).resolve().parent
DOOM2_WAD = EXPERIMENT_DIR.parent / "WADS" / "DOOM2.WAD"
DEFAULT_SCENARIO = Path(vzd.scenarios_path) / "my_way_home.cfg"


def run_demos(run_dir):
    """{generation: [demo paths]} for every recorded generation in a run."""
    gens = {}
    for demo in sorted((run_dir / "recordings").glob("gen_*_episode_*.lmp")):
        gens.setdefault(int(re.match(r"gen_(\d+)_", demo.name).group(1)), []).append(demo)
    return gens


def latest_run():
    """The newest run that has recorded at least one generation, so a run that just started is skipped."""
    runs = sorted((EXPERIMENT_DIR / "training-runs").glob("run-*"), reverse=True)
    if not runs:
        raise SystemExit("no runs found in training-runs/")
    for run_dir in runs:
        if run_demos(run_dir):
            return run_dir
    raise SystemExit("no run in training-runs/ has recorded demos yet")


def generation_demos(run_dir, gen=None):
    gens = run_demos(run_dir)
    if not gens:
        raise SystemExit(f"no demos found in {run_dir / 'recordings'}")
    if gen is None:
        gen = max(gens)
        # The newest generation is still being recorded if it has fewer demos than the one before it
        earlier = [g for g in gens if g < gen]
        if earlier and len(gens[gen]) < len(gens[max(earlier)]):
            print(f"generation {gen} is still recording ({len(gens[gen])} demos so far), using the one before it")
            gen = max(earlier)
    elif gen not in gens:
        raise SystemExit(f"no demos for generation {gen} in {run_dir.name}; recorded: {min(gens)}-{max(gens)}")
    return gen, gens[gen]


def lmp_to_mp4(lmp_path, scenario, iwad, preset):
    """Replay one demo at 720p with the HUD and write it next to the .lmp; returns (mp4 path, total reward)."""
    lmp_path = Path(lmp_path)
    mp4_path = lmp_path.with_suffix(".mp4")

    game = vzd.DoomGame()
    game.load_config(str(scenario))
    if iwad:
        game.set_doom_game_path(str(iwad))
    game.set_screen_resolution(vzd.ScreenResolution.RES_1280X720)
    game.set_render_hud(True)
    game.set_render_corpses(True)
    game.set_window_visible(False)
    game.set_mode(vzd.Mode.SPECTATOR)
    game.init()

    writer = imageio.get_writer(
        mp4_path, fps=35, codec="libx264", quality=None, macro_block_size=8,
        ffmpeg_params=["-crf", "18", "-preset", preset, "-tune", "animation", "-movflags", "+faststart"],
    )
    # ViZDoom hangs on demo paths longer than ~112 characters, so replay from a short temporary copy
    with tempfile.TemporaryDirectory(prefix="lmp") as tmp:
        short_lmp = Path(tmp) / "demo.lmp"
        shutil.copy2(lmp_path, short_lmp)
        try:
            game.replay_episode(str(short_lmp))
            while not game.is_episode_finished():
                state = game.get_state()
                if state is not None:
                    writer.append_data(np.transpose(state.screen_buffer, (1, 2, 0)))
                game.advance_action()
            reward = game.get_total_reward()
        finally:
            writer.close()
            game.close()
    return mp4_path, reward


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("lmps", nargs="*", type=Path, help="demos to convert; defaults to a generation of a run")
    parser.add_argument("--run", help="run folder name in training-runs/, defaults to the latest with demos")
    parser.add_argument("--gen", type=int, help="generation to convert, defaults to the latest fully recorded")
    parser.add_argument("--scenario", type=Path, default=DEFAULT_SCENARIO, help="scenario .cfg the demos were recorded on")
    parser.add_argument("--freedoom", action="store_true", help="replay with Freedoom instead of WADS/DOOM2.WAD")
    parser.add_argument("--preset", default="fast", help="x264 preset; the notebook uses veryslow for smaller files")
    args = parser.parse_args()

    if args.lmps:
        demos = args.lmps
    else:
        run_dir = EXPERIMENT_DIR / "training-runs" / args.run if args.run else latest_run()
        gen, demos = generation_demos(run_dir, args.gen)
        print(f"{run_dir.name}, generation {gen}: {len(demos)} demos")

    # Demos only replay correctly with the IWAD they were recorded with
    iwad = None if args.freedoom or not DOOM2_WAD.is_file() else DOOM2_WAD
    print("IWAD:", iwad.name if iwad else "freedoom2")
    for demo in demos:
        mp4, reward = lmp_to_mp4(demo, args.scenario, iwad, args.preset)
        print(f"{demo.name}  reward={reward:.2f}  -> {mp4}")


if __name__ == "__main__":
    main()
