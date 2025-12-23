# main.py
import os
from experiments import benchmark_solvers, backtest, scalability

def run_all():
    # Ensure plots folder exists
    os.makedirs("plots", exist_ok=True)

    print("\n=== Running Benchmark Solvers ===")
    benchmark_solvers.run_benchmark()

    print("\n=== Running Backtest ===")
    backtest.run_backtest()

    print("\n=== Running Scalability Tests ===")
    scalability.run_scalability()

    print("\nAll experiments completed. Plots saved in ./plots/")

if __name__ == "__main__":
    run_all()
