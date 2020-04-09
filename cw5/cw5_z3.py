class Ksztalty:

    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, x):
        return Kwadrat(self.x + x)

    def __lt__(self, a):
        if self.x < a.x:
            return "Bok pierwszego kwadratu jest mniejszy od boku drugiego kwadratu"
        return "Bok pierwszego kwadratu nie jest mniejszy od boku drugiego kwadratu"
    
    def __le__(self, a):
        if self.x <= a.x:
            return "Bok pierwszego kwadratu jest mniejszy lub rowny bokowi drugiego kwadratu"
        return "Bok pierwszego kwadratu nie jest, ani mniejszy, ani rowny bokowi drugiego kwadratu"

    def __gt__(self, a):
        if self.x > a.x:
            return "Bok pierwszego kwadratu jest wiekszy od boku drugiego kwadratu"
        return "Bok pierwszego kwadratu nie jest wiekszy od boku drugiego kwadratu"
    
    def __ge__(self, a):
        if self.x >= a.x:
            return "Bok pierwszego kwadratu jest wiekszy lub rowny bokowi drugiego kwadratu"
        return "Bok pierwszego kwadratu nie jest, ani wiekszy, ani rowny bokowi drugiego kwadratu"

# lt(a,b) a < b
# le(a,b) a <= b
# eq(a,b) a == b
# ne(a,b) a != b
# gt(a,b) a > b
# ge(a,b) a >= b

kwadrat1 = Kwadrat(4)
kwadrat2 = Kwadrat(5)

print(kwadrat1 < kwadrat2)
print(kwadrat1 <= kwadrat2)
print(kwadrat1 > kwadrat2)
print(kwadrat1 >= kwadrat2)