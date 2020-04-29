import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")

# Unikalne nazwiska sprzedawcow
df_1 = df["Sprzedawca"].unique()

# 5 najwyzszych wartosci zamowien
df_2 = df.nlargest(5, ["Utarg"])

# Ilosc zamowien zlozonych przez kazdego sprzedawce
df_3 = df.groupby("Sprzedawca")["idZamowienia"].count()

# Suma zamowien dla kazdego kraju
df_4 = df.groupby("Kraj")["idZamowienia"].count()

# Suma zamowien dla roku 2005 dla sprzedawcow z Polski
df_5 = df[((df["Data zamowienia"].str.contains("2005")) & (df["Kraj"] == "Polska"))]["idZamowienia"].count()

# Srednia kwota zamowien w 2004 roku
df_6 = df[df["Data zamowienia"].str.contains("2004")]["Utarg"].mean()

# Zapis danych z 2004 do pliku zamowienia_2004.csv oraz danych z 2005 do zamowienia_2005.csv
df[df["Data zamowienia"].str.contains("2004")].to_csv("zamowienia_2004.csv", index=False, sep=";")
df[df["Data zamowienia"].str.contains("2005")].to_csv("zamowienia_2005.csv", index=False, sep=";")

####

print(df)
