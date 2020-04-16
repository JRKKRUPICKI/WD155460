import numpy as np

def funkcja(a):
    return np.diag(np.arange(a, 0, step=-1))

print(funkcja(3))