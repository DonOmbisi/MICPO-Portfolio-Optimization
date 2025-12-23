# models/factor_model.py
import numpy as np
import cvxpy as cp

def factor_model_portfolio(mu, B, F, D, K, U):
    """
    Solve factor-model MISOCP relaxation.
    Sigma = B F B^T + D
    """
    n, k = B.shape
    x = cp.Variable(n)
    z = cp.Variable(n)

    # SOC risk constraint
    t = cp.Variable()
    risk_expr = cp.norm(F**0.5 @ B.T @ x)
    
    constraints = [
        cp.sum(x) == 1,
        x >= 0,
        x <= z * U,
        cp.sum(z) <= K,
        z >= 0,
        z <= 1,
        risk_expr <= t
    ]

    prob = cp.Problem(cp.Minimize(t - mu @ x), constraints)
    prob.solve(solver=cp.ECOS, warm_start=True)
    return prob.value, x.value, z.value
