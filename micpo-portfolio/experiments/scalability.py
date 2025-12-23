# experiments/scalability.py
import time
import matplotlib.pyplot as plt
import os
from utils.data_loader import synthetic_data
from models.mean_variance import mean_variance_portfolio

def run_scalability():
    # Ensure plots folder exists
    os.makedirs("plots", exist_ok=True)

    asset_sizes = [100, 500, 1000, 2000]
    solve_times = []

    for n_assets in asset_sizes:
        mu, Sigma = synthetic_data(n_assets)
        K = min(20, n_assets // 5)
        U = 0.2

        start = time.time()
        val, x, z = mean_variance_portfolio(mu, Sigma, K, U)
        end = time.time()

        solve_times.append(end - start)
        print(f"{n_assets} assets: Solve time={end-start:.2f}s, Relaxation value={val:.4f}")

    # Plot and save
    plt.figure(figsize=(6, 4))
    plt.plot(asset_sizes, solve_times, marker='o')
    plt.xlabel("Number of Assets")
    plt.ylabel("Solve Time (s)")
    plt.title("Runtime Scaling of MIQP Relaxation")
    plt.grid(True)
    plt.savefig(os.path.join("plots", "runtime_scaling.png"))
    plt.close()

if __name__ == "__main__":
    run_scalability()

