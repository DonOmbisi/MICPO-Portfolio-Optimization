# solver/cuts.py

def cardinality_cut(z, indices):
    """
    Generate a cardinality cut: sum(z[i] for i in indices) <= len(indices)-1
    """
    return sum(z[i] for i in indices) <= len(indices)-1

def perspective_cut(xi, zi, yi):
    """
    Perspective cut: yi >= xi^2 / zi
    """
    if zi > 0:
        return yi >= xi**2 / zi
    return True  # inactive if zi == 0
