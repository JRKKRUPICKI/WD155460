# (x - a)^2 + (y - b)^2 = r^2
def funkcja(a = 0, b = 0, x = 0, y = 0):
    return ((x - a) ** 2 + (y - b) ** 2) ** (1/2)

print(funkcja(1, 3, 1, 1))