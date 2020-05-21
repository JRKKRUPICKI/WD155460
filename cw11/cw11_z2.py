import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

ax = plt.subplot(111, projection="3d")

color = ["r", "b", "m", "c", "g"]
marker = [".", "h", "X", "D", "*"]

for i in range(5):
    x = (100 - 0) * np.random.rand(100) + 0
    y = (100 - 0) * np.random.rand(100) + 0
    z = (100 - 0) * np.random.rand(100) + 0
    ax.scatter(x, y, z, c=color[i], marker=marker[i])

plt.show()
