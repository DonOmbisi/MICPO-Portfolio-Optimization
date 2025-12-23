# solver/cholesky_cache.py
import numpy as np

class CholeskyCache:
    def __init__(self):
        self.cache = {}

    def get(self, Sigma):
        key = Sigma.tostring()
        if key not in self.cache:
            self.cache[key] = np.linalg.cholesky(Sigma + 1e-8*np.eye(Sigma.shape[0]))
        return self.cache[key]
