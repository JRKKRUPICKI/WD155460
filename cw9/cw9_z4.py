import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv("iris.data", sep=",", names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"])

df_1 = df[df["Class"] == "Iris-setosa"]
df_2 = df[df["Class"] == "Iris-versicolor"]
df_3 = df[df["Class"] == "Iris-virginica"]

s_1 = plt.scatter(df_1["Sepal length"], df_1["Sepal width"], color="r")
s_2 = plt.scatter(df_2["Sepal length"], df_2["Sepal width"], color="g")
s_3 = plt.scatter(df_3["Sepal length"], df_3["Sepal width"], color="b")

plt.ylabel("Sepal length")
plt.xlabel("Sepal width")
plt.title("Sepal for each class")
plt.legend((s_1, s_2, s_3), ("Iris-setosa", "Iris-versicolor", "Iris-virginica"), title="Classes")

plt.show()
