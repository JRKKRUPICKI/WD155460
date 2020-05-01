import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, index_col=None)

grupa = df.groupby(["Plec"]).agg({"Liczba":["sum"]})

wykres = grupa.plot.bar()
wykres.set_ylabel("Liczba urodzonych")
wykres.set_xlabel("Plec")
wykres.legend()
plt.title("Liczba urodzonych z podzialem na plec")
plt.show()
