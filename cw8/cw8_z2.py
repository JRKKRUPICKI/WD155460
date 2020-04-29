import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, index_col=None)

# Rekordy z liczba nadanych imion w danym roku wieksza niz 1000
df_1 = df[df["Liczba"] > 1000]

# Rekordy z imieniem JAROSŁAW
df_2 = df[df["Imie"] == "JAROSŁAW"]

# Suma wszystkich urodzonych dzieci
df_3 = df["Liczba"].sum()

# Suma dzieci urodzonych w latach 2000 - 2005
df_4 = df[(df["Rok"] >= 2000) & (df["Rok"] <= 2005)]
df_4_1 = df_4["Liczba"].sum()

# Suma urodzonych dzieci (plec meska i zenska osobno)
df_5_M = df[df["Plec"] == "M"]
df_5_K = df[df["Plec"] == "K"]
df_5_M_suma = df_5_M["Liczba"].sum()
df_5_K_suma = df_5_K["Liczba"].sum()

# Najpopularniejsze imie w danym roku (plec meska i zenska osobno)
df_6 = df.copy()
df_6["LiczbaMax"] = df.groupby(by=["Rok", "Plec"])["Liczba"].transform(max)
df_6_imie = df_6[df_6["Liczba"] == df_6["LiczbaMax"]]

# Najpopularniejsze imie w calym okresie (plec meska i zenska osobno)
df_7 = df.copy()
df_7["LiczbaMax"] = df.groupby(by="Rok")["Liczba"].transform(max)
df_7_imie = df_7[df_7["Liczba"] == df_7["LiczbaMax"]]

####

print(df_7_imie)
