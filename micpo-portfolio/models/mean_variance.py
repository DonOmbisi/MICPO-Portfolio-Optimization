# models/mean_variance.py
import numpy as np
import cvxpy as cp
from solver.relaxations import qp_relaxation

def mean_variance_portfolio(mu, Sigma, K, U):
    """
    Solve basic mean-variance MIQP relaxation.
    Wrap Sigma with psd_wrap to avoid ARPACK convergence errors.
    """
    # Ensure Sigma is treated as PSD to avoid ARPACK errors
    Sigma_psd = cp.psd_wrap(Sigma)

    value, x, z = qp_relaxation(mu, Sigma_psd, K, U)
    return value, x, z
