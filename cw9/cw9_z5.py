import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv("zamowienia.csv", sep=";")

grupa = df.groupby("Sprzedawca").agg({"idZamowienia":["count"]})

wykres = grupa.plot.bar()
wykres.set_ylabel("Liczba zamowien")
wykres.set_xlabel("Sprzedawca")
wykres.legend()
plt.title("Liczba zlozonych zamowien przez danych sprzedawcow")
plt.show()
