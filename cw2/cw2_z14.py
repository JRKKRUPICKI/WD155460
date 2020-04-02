from math import *

a = int(input("a: "))
try:
	print(sqrt(a))
except ValueError:
	print("Pierwiastkowana liczba nie moze byc ujemna")