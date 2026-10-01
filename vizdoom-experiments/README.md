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

- `basic-dqn/` — Rainbow DQN on ViZDoom Basic
- `deadly-corridor-dqn/` — Rainbow DQN on Deadly Corridor

Defend the Center and Defend the Line have scenarios and no notebook yet, so they are `defend-the-center/` and `defend-the-line/` until a technique is added.
