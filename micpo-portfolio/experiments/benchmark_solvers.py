# experiments/benchmark_solvers.py
import os
import matplotlib.pyplot as plt
from utils.data_loader import synthetic_data
from models.mean_variance import mean_variance_portfolio

def run_benchmark():
    asset_sizes = [100, 300, 500, 1000]
    relaxation_values = []
    greedy_values = []

    for n_assets in asset_sizes:
        mu, Sigma = synthetic_data(n_assets)
        K = min(20, n_assets // 5)
        U = 0.2

        val, x, z = mean_variance_portfolio(mu, Sigma, K, U)

        # Greedy heuristic (simplified example)
        greedy_val = mu[:K].sum()

        relaxation_values.append(val)
        greedy_values.append(greedy_val)

        print(f"{n_assets} assets: Relaxation value={val:.4f}")
        print(f"{n_assets} assets: Greedy heuristic value={greedy_val:.4f}")

    # Ensure plots folder exists
    os.makedirs("plots", exist_ok=True)

    # Save plot
    plt.figure(figsize=(6,4))
    plt.plot(asset_sizes, relaxation_values, marker='o', label="Relaxation")
    plt.plot(asset_sizes, greedy_values, marker='x', label="Greedy heuristic")
    plt.xlabel("Number of Assets")
    plt.ylabel("Objective Value")
    plt.title("Benchmark Solvers Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("plots/benchmark_solvers.png")
    plt.close()

if __name__ == "__main__":
    run_benchmark()
