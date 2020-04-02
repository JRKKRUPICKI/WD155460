import sys

for i in range(1, 11, 1):
	for j in range(1, 11, 1):
		w = str(i * j)
		if len(w) == 1:
			w = "  " + w
		if len(w) == 2:
			w = " " + w
		sys.stdout.write(w)
		if j != 10:
			sys.stdout.write(" ")
	sys.stdout.write("\n")