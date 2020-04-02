a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if 0 < a <= 10 and (a > b or b > c):
	print("Warunki spelnione")
else:
	print("Warunki niespelnione")