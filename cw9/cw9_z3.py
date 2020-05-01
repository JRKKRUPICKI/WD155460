import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, index_col=None)

ostatnie_5_lat = df[((df["Rok"] <= 2017) & (df["Rok"] >= 2013))]
grupa = ostatnie_5_lat.groupby(["Plec"]).agg({"Liczba":["sum"]})

wykres = grupa.plot.pie(subplots=True, autopct="%.2f %%")
plt.title("Procent sumy urodzonych z podzialem na plec z ostatnich 5 lat")
plt.show()
