# solver/heuristics.py
import numpy as np


def greedy_heuristic(mu, Sigma, K):
    scores = mu / np.sqrt(np.diag(Sigma))
    idx = np.argsort(scores)[-K:]
    x = np.zeros(len(mu))
    x[idx] = 1 / K
    return x