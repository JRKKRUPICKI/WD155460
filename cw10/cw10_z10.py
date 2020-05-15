import matplotlib.pyplot as plt
import numpy as np

# Wykres z zadania 1

plt.subplot(211)

x = np.arange(1, 21)

plt.plot(x, 1/x, label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.xlim(1,len(x))
plt.ylim(0,1)

plt.annotate('punkt: x = 5, y = 0.2)',
            xy=(5, 0.2), xycoords='data',
            xytext=(120, 30), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')


# Wykres z zadania 2

plt.subplot(212)

y = np.arange(1, 21)

plt.plot(x, 1/x, "g>:", label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.ylim(0,1)

plt.annotate('punkt: x = 10, y = 0.1)',
            xy=(10, 0.1), xycoords='data',
            xytext=(130, 20), textcoords='offset points',
            arrowprops=dict(facecolor='g', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')

plt.show()
