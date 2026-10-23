# ViZDoom experiments

These are the ViZDoom runs. The agents learn from pixels with AgileRL, and each experiment is its own notebook. They run locally in this repo, or on Colab if that's easier. 

Each notebook will also try to load the original Doom wad if it is present. It will look in the `WADS/` directory for `DOOM2.WAD` (full path: `rl-epsilon/vizdoom-agilerl-experiments/WADS/DOOM2.WAD`). Sadly I can't redistribute the wad in this repo, but it's easy to get by purchasing the game on [Steam](https://store.steampowered.com/app/2300/DOOM_II/).

If `DOOM2.WAD` isn't present, it will fall back to the Freedoom assets, which ship with ViZDoom by default. But personally I think the original assets are preferable if you can get your hands on them.

Each notebook will produce several checkpoints and eval videos for analyzing how the model did. Only a handful are committed, and those can be found in the experiment's artifacts directory. Each run will store its individual outputs in a timestamped run directory generated at runtime, which is not committed.

Directory layout:
```
experiment/
├── <notebook>.ipynb
├── scenario_files/
├── artifacts/
│   ├── model/
│   ├── video/
│   └── plots_and_figures/
└── training-runs/             # not committed
    └── run-<timestamp>/
        ├── checkpoints/
        ├── recordings/
        └── video/
```

## Experiments

| Experiment | Algorithm | Objective |
| --- | --- | --- |
| [Basic](basic-dqn-AgileRL/AgileRL_DQN_DoomBasic_TrainEval.ipynb) | DQN | Exploring AgileRL's DQN implementation. [Basic](https://vizdoom.farama.org/environments/default/#basic) is one room and one monster. The agent can only move side to side and shoot. |
| [Deadly Corridor](deadly-corridor-dqn-AgileRL/AgileRL_DQN_DoomDeadlyCorridor_TrainEval.ipynb) | Double DQN | Exploring AgileRL's Double DQN implementation. [Deadly Corridor](https://vizdoom.farama.org/environments/default/#deadly-corridor) is a hallway with monsters on both sides and a vest at the far end. |
| [Defend the Center](defend-the-center-ppo-AgileRL/AgileRL_PPO_DoomDefendTheCenter_TrainEval.ipynb) | PPO | Exploring AgileRL's PPO implementation. [Defend the Center](https://vizdoom.farama.org/environments/default/#defend-the-center) is a circular room. Ammo is limited, and enemies come in from every side and continually spawn. |
| [Defend the Line](defend-the-line-ppo-AgileRL/AgileRL_PPO_DoomDefendTheLine_TrainEval.ipynb) | PPO | Exploring AgileRL's PPO implementation. [Defend the Line](https://vizdoom.farama.org/environments/default/#defend-the-line) has melee demons and shooting demons continually spawning at the end of a hall. The agent can only turn and shoot. |
| [Defend the Line, strafing](defend-the-line-strafe-ppo-AgileRL/AgileRL_PPO_DoomDefendTheLineStrafe_TrainEval.ipynb) | PPO | Modification of the `Defend the Line` scenario, exploring how the model behavior changes when the agent can strafe, specifically if it can learn to dodge the projectiles. The room is still [Defend the Line](https://vizdoom.farama.org/environments/default/#defend-the-line). |
| [My Way Home](my-way-home-ppo-icm-AgileRL/AgileRL_PPO_ICM_DoomMyWayHome_TrainEval.ipynb) | PPO + ICM | Curiosity-driven exploration with an Intrinsic Curiosity Module on top of AgileRL's PPO, using a custom training loop. [My Way Home](https://vizdoom.farama.org/environments/default/#my-way-home) is a maze of colored rooms. Doomguy starts in a random one, and the vest is always in the same room. |
| [My Way Home, PyTorch](my-way-home-ppo-icm-pytorch/PyTorch_PPO_ICM_DoomMyWayHome_TrainEval.ipynb) | PPO + ICM | The same curiosity experiment without AgileRL: a small, modular PPO and ICM written in plain PyTorch. The maze is still [My Way Home](https://vizdoom.farama.org/environments/default/#my-way-home). |
| [My Way Home, RND](my-way-home-ppo-rnd-pytorch/PyTorch_PPO_RND_DoomMyWayHome_TrainEval.ipynb) | PPO + RND | Novelty-driven exploration with Random Network Distillation on the stock maze, with no reward shaping, in plain PyTorch. The maze is still [My Way Home](https://vizdoom.farama.org/environments/default/#my-way-home). |

