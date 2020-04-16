import numpy as np

def funkcja(n):
    return np.arange(1, n * n + 1).reshape((n, n))

print(funkcja(3))