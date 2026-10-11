# VizDoom experiments

Pixel-observation experiments on ViZDoom. Each experiment is self-contained and named scenario, then technique. Commercial IWADs belong in `WADS/` and are not committed.

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

- `basic-dqn/` — DQN on ViZDoom Basic
- `deadly-corridor-dqn/` — Double DQN on Deadly Corridor
- `defend-the-center-ppo-AgileRL/` — PPO on Defend the Center
- `defend-the-line-ppo-AgileRL/` — PPO on Defend the Line
- `defend-the-line-strafe-ppo-AgileRL/` — PPO on Defend the Line, with sidestepping
