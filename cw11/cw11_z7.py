import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

ax = plt.subplot(111, projection="3d")

x = (100 - 0) * np.random.rand(20) + 0
y = (100 - 0) * np.random.rand(20) + 0
z = (100 - 0) * np.random.rand(20) + 0
ax.scatter(x, y, z, c="r", label="Jablko")

x = (100 - 0) * np.random.rand(5) + 0
y = (100 - 0) * np.random.rand(5) + 0
z = (100 - 0) * np.random.rand(5) + 0
ax.plot(x, y, z, c="g", label="Waz")

plt.legend()
plt.title("Snake")

plt.show()
