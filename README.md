# rl-epsilon

A collection of small one-shot reinforcement learning experiments.

I wanted a place where I could share the various small experiments that I run without having dozens of small repositories cluttering up my page. So the intention of this repo is to have all the small scale projects and experiments in one place!

Each experiment explores some aspect of reinforcement learning, such as a new library, a new environment, or a new technique if the implementation isn't too complex. If a project grows in scale or complexity it will get spun out into its own dedicated repo!

## How it's laid out
Overall the organization in this repository might be a bit loose since it is a collection of individual 
experiments, but there is a rough organizational method.

Experiments are grouped by environment. All the ViZDoom ones live together in one directory. When I get to StableRetro, that'll be its own directory too.

The directory name lists the scenario, the technique (DQN, PPO), and a short note about what's being tried.

## Experiments

- [ViZDoom](vizdoom-agilerl-experiments/README.md) — agents that learn ViZDoom from pixels, using AgileRL
