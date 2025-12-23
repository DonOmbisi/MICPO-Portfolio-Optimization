# solver/branch_and_bound.py
import numpy as np
from solver.relaxations import qp_relaxation
from solver.heuristics import greedy_heuristic


class Node:
    def __init__(self, fixed):
        self.fixed = fixed # {index: 0 or 1}


class BranchAndBound:
    def __init__(self, mu, Sigma, K, U):
        self.mu = mu
        self.Sigma = Sigma
        self.K = K
        self.U = U
        self.best_val = np.inf
        self.best_x = None


def solve(self):
    root = Node({})
    self._branch(root)
    return self.best_val, self.best_x


def _branch(self, node):
    val, x, z = qp_relaxation(self.mu, self.Sigma, self.K, self.U)
    if val >= self.best_val:
        return


    fractional = [i for i in range(len(z)) if abs(z[i] - round(z[i])) > 1e-3]
    if not fractional:
        self.best_val = val
        self.best_x = x
        return


    i = fractional[0]
    for v in [0, 1]:
        child = Node({**node.fixed, i: v})
        self._branch(child)