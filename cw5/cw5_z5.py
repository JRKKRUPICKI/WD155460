class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print("#### isinstance ####")
print(isinstance(jozek, Osoba))
print(isinstance(jozek, Pracownik))
print(isinstance(jozek, Menadzer))
print("####")
print(isinstance(adrian, Osoba))
print(isinstance(adrian, Pracownik))
print(isinstance(adrian, Menadzer))
print("#### issubclass ####")
print(issubclass(Pracownik, Osoba))
print(issubclass(Pracownik, Pracownik))
print(issubclass(Pracownik, Menadzer))
print("####")
print(issubclass(Menadzer, Osoba))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Menadzer, Menadzer))