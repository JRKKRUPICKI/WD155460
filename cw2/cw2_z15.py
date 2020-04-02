try:
	int(input("Podaj liczbe: "))
	print("OK")
except ValueError:
	print("Wpisano cos co nie jest liczba")