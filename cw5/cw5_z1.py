class Material:
    
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)

class Ubrania(Material):
    
    def __init__(self, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_dane(self):
        print(f"{self.rozmiar} | {self.kolor} | {self.dla_kogo} | {self.rodzaj} | {self.dlugosc} | {self.szerokosc}")

class Sweter(Ubrania):
    
    def __init__(self, rodzaj_swetra, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        self.rodzaj_swetra = rodzaj_swetra
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_dane(self):
        print(f"{self.rodzaj_swetra} | {self.rozmiar} | {self.kolor} | {self.dla_kogo} | {self.rodzaj} | {self.dlugosc} | {self.szerokosc}")


sweter = Sweter("rozpinany", "L", "czarny", "Klient", "bawelna", 100, 60)
sweter.wyswietl_dane()

material = Material("bawelna", 50, 30)
material.wyswietl_nazwe()

ubranie = Ubrania("XL", "niebieski", "Klient", "bawelna", 80, 40)
ubranie.wyswietl_dane()