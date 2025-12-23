#!/bin/bash
# run_experiments.sh


# Ensure deterministic seeds
export PYTHONHASHSEED=42


# Build Docker image
docker build -t micpo .


# Run experiments
docker run --rm micpo python3 experiments/benchmark_solvers.py
docker run --rm micpo python3 experiments/backtest.py
docker run --rm micpo python3 experiments/scalability.py