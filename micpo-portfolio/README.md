MICPO Portfolio Optimization

A Python project for portfolio optimization experiments using MIQP relaxations, including benchmarking, backtesting, and scalability testing. Fully Dockerized for easy reproducibility.

Project Structure
micpo-portfolio/
├─ cpp/                   # Optional C++ components (if any)
├─ data/                  # Sample datasets
├─ docker/                # Docker-related files
├─ experiments/           # Scripts to run experiments
│  ├─ benchmark_solvers.py
│  ├─ backtest.py
│  └─ scalability.py
├─ models/                # Python models (mean-variance, etc.)
├─ solver/                # Solver implementations and relaxations
├─ utils/                 # Utility scripts (data loaders, helpers)
├─ plots/                 # Generated plots from experiments
├─ requirements.txt       # Python dependencies
├─ main.py                # Run all experiments sequentially
├─ Dockerfile
├─ docker-compose.yml
├─ run_experiments.sh     # Optional convenience script
└─ README.md

Setup and Installation

Clone the repository:

git clone <your-repo-url>
cd micpo-portfolio


Build the Docker image:

docker build -t micpo .


This installs all dependencies and sets up a Python environment inside a container.

Running Experiments

All experiments automatically save plots in the plots/ folder.

1. Run All Experiments
docker run --rm -e PYTHONPATH=/micpo-portfolio \
  -v $(pwd)/plots:/micpo-portfolio/plots \
  micpo python3 main.py


-e PYTHONPATH=/micpo-portfolio ensures Python can find all modules.

-v $(pwd)/plots:/micpo-portfolio/plots mounts the plots/ folder so generated plots appear on your host.

2. Run Benchmark Solvers Only
docker run --rm -e PYTHONPATH=/micpo-portfolio micpo \
  python3 experiments/benchmark_solvers.py

3. Run Backtest Only
docker run --rm -e PYTHONPATH=/micpo-portfolio micpo \
  python3 experiments/backtest.py

4. Run Scalability Test Only
docker run --rm -e PYTHONPATH=/micpo-portfolio \
  -v $(pwd)/plots:/micpo-portfolio/plots \
  micpo python3 experiments/scalability.py


Generates runtime_scaling.png inside the plots/ folder.

Plot Output

After running experiments, your plots/ folder will contain:

plots/
├─ backtest.png
├─ benchmark_solvers.png
└─ runtime_scaling.png

Development Notes

All scripts assume a Python 3.10+ environment.

Ensure PYTHONPATH=/micpo-portfolio is set when running scripts inside Docker.

For faster runs, reduce the number of assets in experiments/scalability.py.

Optional: Run Locally without Docker

Create a Python virtual environment:

python3 -m venv myenv
source myenv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run experiments directly:

python main.py


Note: Docker is recommended to ensure reproducibility and avoid library conflicts.