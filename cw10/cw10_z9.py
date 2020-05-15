import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

df = pd.read_csv("zamowienia.csv", sep=";")

dane = df.groupby("Sprzedawca")["Utarg"].sum().reset_index()

explode = [0 for i in range(len(dane["Sprzedawca"]))]
explode[random.randint(0, len(dane["Sprzedawca"]) - 1)] = 0.3

plt.figure(figsize=(7,5))
wedges, texts, autotexts = plt.pie(dane["Utarg"], labels=dane["Sprzedawca"],
    autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color="black"), shadow=True, explode=explode)
plt.setp(autotexts, size=12, weight="bold")
plt.title("Procent udziałów sprzedawców")
plt.legend(title="Sprzedawcy", bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0.)
plt.show()
