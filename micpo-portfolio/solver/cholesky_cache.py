# solver/cholesky_cache.py
import numpy as np

class CholeskyCache:
    def __init__(self):
        self.cache = {}

    def get(self, Sigma):
        key = Sigma.tobytes()
        if key not in self.cache:
            self.cache[key] = np.linalg.cholesky(Sigma)
        return self.cache[key]
