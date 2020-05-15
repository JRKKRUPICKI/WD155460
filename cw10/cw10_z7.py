import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, index_col=None)

dane_wykres_1 = df.groupby("Plec")["Liczba"].sum().reset_index()
dane_wykres_2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
dane_wykres_2_K = dane_wykres_2[dane_wykres_2["Plec"] == "K"].reset_index()
dane_wykres_2_M = dane_wykres_2[dane_wykres_2["Plec"] == "M"].reset_index()
dane_wykres_2 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
dane_wykres_3 = df.groupby("Rok")["Liczba"].sum().reset_index()

plt.subplot(131)
plt.bar(dane_wykres_1["Plec"], dane_wykres_1["Liczba"], color=["orange", "yellow"])
plt.xlabel("Plec")
plt.ylabel("Liczba urodzonych")

plt.subplot(132)
plt.bar(dane_wykres_2_K["Rok"], dane_wykres_2_K["Liczba"], color="blue", label="K")
plt.bar(dane_wykres_2_M["Rok"], dane_wykres_2_M["Liczba"], color="red", label="M", bottom=dane_wykres_2_K["Liczba"])
plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")
plt.legend()

plt.subplot(133)
plt.bar(dane_wykres_3["Rok"], dane_wykres_3["Liczba"], color="c")
plt.xlabel("Rok")
plt.ylabel("Liczba urodzonych")

plt.suptitle("Liczba urodzonych K i M")

plt.show()
