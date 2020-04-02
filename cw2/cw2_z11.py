wysokosc = int(input("Wysokosc: "))

if wysokosc < 3:
	wysokosc = 3
if wysokosc > 9:
	wysokosc = 9

n = 0
for i in range(1,  wysokosc + 1):
	for j in range(1, (wysokosc - i) + 1):
		print(end = " ")
	while n != (2 * i - 1):
		print("*", end = "")
		n += 1
	n = 0
	print()
k = 1
n = 1
for i in range(1,  wysokosc):
	for j in range(1, k + 1):
		print(end = " ")
	k += 1
	while n <= 2 * (wysokosc - i) - 1:
		print("*", end = "")
		n += 1
	n = 1
	print()