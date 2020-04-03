plik = open("cw4_z1.txt", "w+")
for i in range(4, 1000, 4):
    plik.write(str(i) + "\n")
plik.close()