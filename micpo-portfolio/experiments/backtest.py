# experiments/backtest.py
import os
import matplotlib.pyplot as plt
import numpy as np
from utils.data_loader import synthetic_data
from models.mean_variance import mean_variance_portfolio

def run_backtest():
    n_assets = 100
    mu, Sigma = synthetic_data(n_assets)
    K = min(20, n_assets // 5)
    U = 0.2

    val, x, z = mean_variance_portfolio(mu, Sigma, K, U)

    # Simulate a simple portfolio wealth evolution
    returns = np.random.multivariate_normal(mu, Sigma, 252)  # 252 trading days
    portfolio_returns = returns @ x
    wealth = np.cumprod(1 + portfolio_returns)

    final_wealth = wealth[-1]
    sharpe_ratio = portfolio_returns.mean() / portfolio_returns.std()
    max_drawdown = np.max(np.maximum.accumulate(wealth) - wealth)

    print(f"Final wealth: {final_wealth:.4f}")
    print(f"Sharpe ratio: {sharpe_ratio:.4f}")
    print(f"Max drawdown: {max_drawdown:.4f}")

    # Ensure plots folder exists
    os.makedirs("plots", exist_ok=True)

    # Save wealth evolution plot
    plt.figure(figsize=(6,4))
    plt.plot(wealth)
    plt.xlabel("Days")
    plt.ylabel("Portfolio Wealth")
    plt.title("Portfolio Backtest")
    plt.grid(True)
    plt.savefig("plots/backtest.png")
    plt.close()

if __name__ == "__main__":
    run_backtest()
