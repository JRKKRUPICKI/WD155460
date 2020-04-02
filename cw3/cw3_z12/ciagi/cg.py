def n_wyraz(a1, q, n):
    return a1 * q ** (n - 1)

def suma_n_wyrazow(a1, q, n):
    if q == 1:
        return a1 * n
    return a1 * (1 - q ** n) / (1 - q)
