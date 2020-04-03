import sys

print("Zapis:")

with open("cw4_z3.txt", "w+") as plik:
    for i in range(0, 3):
        plik.write(sys.stdin.readline())

print("Odczyt:")

with open("cw4_z3.txt", "r") as plik:
    for i in plik.readlines():
        print(i, end="")