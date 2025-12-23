# solver/relaxations.py
import cvxpy as cp
import numpy as np

def qp_relaxation(mu, Sigma, K, U):
    n = len(mu)
    x = cp.Variable(n)
    z = cp.Variable(n)

    risk = cp.quad_form(x, Sigma)
    ret = mu @ x

    constraints = [
        cp.sum(x) == 1,
        x >= 0,
        x <= z * U,
        cp.sum(z) <= K,
        z >= 0,
        z <= 1
    ]

    prob = cp.Problem(cp.Minimize(risk - ret), constraints)
    prob.solve(solver=cp.OSQP, warm_start=True)
    return prob.value, x.value, z.value
