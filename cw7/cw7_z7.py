import numpy as np

a = np.sin(np.array([3,1,7,9,2,0]).reshape(2,3))
b = np.cos(np.array([3,1,7,9,2,0]).reshape(2,3))

print(a)
print(b)
print(np.add(a, b))
