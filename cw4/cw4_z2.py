plik = open("cw4_z1.txt", "r")
for wiersz in plik.readlines():
    print(wiersz, end="")
plik.close()