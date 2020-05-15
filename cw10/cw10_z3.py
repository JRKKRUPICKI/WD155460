import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30.1, 0.1)
s = np.sin(x)
c = np.cos(x)

plt.plot(x, s, "b", label="sin(x)")
plt.plot(x, c, "c", label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Wykres funkcji sin(x) i cos(x) dla x [0, 30]")
plt.show()
