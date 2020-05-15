import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("iris.data", sep=",", names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"])

data = {
    "a": df["Sepal length"],
    "b": df["Sepal width"],
    "c": np.random.randint(0, 50, 150)
}
data["d"] = np.abs(data["a"] - data["b"])

plt.scatter("a", "b", c="c", s="d", data=data)
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()
