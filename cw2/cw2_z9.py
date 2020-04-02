while(True):
	a = int(input("a: "))
	wynik = 0
	b = a % 10
	while(b > 0):
		wynik += b
		a = a // 10
		b = a % 10
	print(wynik)