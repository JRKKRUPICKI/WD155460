class Robaczek:

    x = 0
    y = 0
    krok = 1

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    
    def idz_w_gore(self, ile_krokow):
        self.y += self.krok * ile_krokow
    
    def idz_w_dol(self, ile_krokow):
        self.y -= self.krok * ile_krokow
    
    def idz_w_lewo(self, ile_krokow):
        self.x -= self.krok * ile_krokow
    
    def idz_w_prawo(self, ile_krokow):
        self.x += self.krok * ile_krokow
    
    def pokaz_gdzie_jestes(self):
        print(f"x: {self.x}, y: {self.y}")

robak = Robaczek(0, 0, 1)
robak.idz_w_gore(3)
robak.idz_w_dol(2)
robak.idz_w_lewo(4)
robak.idz_w_prawo(8)
robak.pokaz_gdzie_jestes()