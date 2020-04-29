import numpy as np

a = np.array([3,5,7,9,4,7,1,0,2]).reshape(3,3)
b = np.arange(16).reshape(4,4)

print(a)
print(b)

print(a.min(axis=0))
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))