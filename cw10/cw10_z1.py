import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 21)

plt.plot(x, 1/x, label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.xlim(1,len(x))
plt.ylim(0,1)
plt.show()
