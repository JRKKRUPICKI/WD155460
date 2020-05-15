import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30.1, 0.1)
s1 = np.sin(x) + 2
s2 = np.sin(x) * -1

plt.plot(x, s1, "#1872b1", label="sin(x)")
plt.plot(x, s2, "#ff861b", label="sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend(loc="center left")
plt.title("Wykres sin(x), sin(x)")
plt.show()
