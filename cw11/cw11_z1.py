import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.figure().gca(projection = "3d")

z = np.linspace(0, 2*np.pi, 100)
x = np.sin(z)
y = 2*np.cos(z)

plt.plot(x, y, z)
plt.show()