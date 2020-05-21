import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize =(8, 3))
ax1 = plt.subplot(231, projection="3d")
ax2 = plt.subplot(232, projection="3d")
ax3 = plt.subplot(233, projection="3d")
ax4 = plt.subplot(234, projection="3d")
ax5 = plt.subplot(235, projection="3d")
ax6 = plt.subplot(236, projection="3d")

_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax2.bar3d(x, y, bottom, width, depth, top, shade=True, color="m")
ax3.bar3d(x, y, bottom, width, depth, top, shade=True, color="c")
ax4.bar3d(x, y, bottom, width, depth, top, shade=True, color="r")
ax5.bar3d(x, y, bottom, width, depth, top, shade=True, color="g")
ax6.bar3d(x, y, bottom, width, depth, top, shade=True, color="b")
plt.show()
