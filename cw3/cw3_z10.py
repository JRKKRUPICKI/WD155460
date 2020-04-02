def funkcja(**lista):
    ilosc = 0
    for i in lista:
        ilosc += lista[i]
    return ilosc

print(funkcja(chleb=2, rogalik=4, ziemniaki=10))