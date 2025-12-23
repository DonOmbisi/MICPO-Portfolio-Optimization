# utils/data_loader.py
import numpy as np

def synthetic_data(n, factors=5, seed=42):
    np.random.seed(seed)
    B = np.random.randn(n, factors)
    F = np.diag(np.random.rand(factors))
    D = np.diag(np.random.rand(n) * 0.05)
    Sigma = B @ F @ B.T + D
    mu = np.random.randn(n) * 0.05
    return mu, Sigma