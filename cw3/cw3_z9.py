def funkcja(*liczby):
    if len(liczby) == 0:
        return 0
    wynik = 1
    for i in liczby:
        wynik *= i
    return wynik

print(funkcja(1,5,3,4,7,3,6,2))