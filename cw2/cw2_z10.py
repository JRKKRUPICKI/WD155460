import sys

wysokosc = int(input("Wysokosc: "))

if wysokosc > 10:
	wysokosc = 10

for i in range(1, wysokosc + 1, 1):
	for j in range(1, i + 1, 1):
		sys.stdout.write("A")
	sys.stdout.write("\n")