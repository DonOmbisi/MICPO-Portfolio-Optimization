# utils/metrics.py
import numpy as np

def sharpe_ratio(returns):
    mean = np.mean(returns)
    std = np.std(returns)
    return mean / std if std != 0 else 0

def max_drawdown(wealth):
    peak = -np.inf
    max_dd = 0
    for w in wealth:
        if w > peak:
            peak = w
        dd = (peak - w) / peak
        if dd > max_dd:
            max_dd = dd
    return max_dd
