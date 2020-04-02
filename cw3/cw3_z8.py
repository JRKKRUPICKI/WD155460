# Suma ciagu arytmetycznego
# (a1 + an) / 2 * n
# (2 * a1 + (n - 1) * r) / 2 * n
def funkcja(a1 = 1, r = 1, ile_elementow = 10):
    return (2 * a1 + (ile_elementow - 1) * r) / 2 * ile_elementow

print(funkcja())