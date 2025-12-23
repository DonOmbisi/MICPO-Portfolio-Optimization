# models/robust.py
import cvxpy as cp
import numpy as np

def robust_portfolio(mu_hat, Sigma, rho, K, U):
    """
    Ellipsoidal robust mean-variance portfolio.
    """
    n = len(mu_hat)
    x = cp.Variable(n)
    z = cp.Variable(n)

    # Robust worst-case return: -mu^T x + rho * ||Sigma^(1/2) x||_2
    Sigma_sqrt = np.linalg.cholesky(Sigma)
    risk = cp.quad_form(x, Sigma)
    worst_case_return = -mu_hat @ x + rho * cp.norm(Sigma_sqrt @ x)

    constraints = [
        cp.sum(x) == 1,
        x >= 0,
        x <= z * U,
        cp.sum(z) <= K,
        z >= 0,
        z <= 1
    ]

    prob = cp.Problem(cp.Minimize(risk + worst_case_return), constraints)
    prob.solve(solver=cp.ECOS, warm_start=True)
    return prob.value, x.value, z.value
