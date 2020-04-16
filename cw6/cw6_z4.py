import numpy as np

def funkcja(a, b):
    return np.logspace(1, b, base=a, num=b, dtype="int")

print(funkcja(2, 4))