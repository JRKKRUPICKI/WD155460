class Slowa:

    s1 = ""
    s2 = ""

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    
    def __del__(self):
        print("Obiekt zostal usuniety")

    def wyswietl_wyrazy(self):
        print(f"{self.s1} {self.s2}")

    def sprawdz_czy_palindrom(self):
        return self.s1 == self.s2[::-1]
    
    def sprawdz_czy_metagramy(self):
        if len(self.s1) == len(self.s2):
            r = 0
            for i in range(0, len(self.s1)):
                if self.s1[i] != self.s2[i]:
                    r += 1
            if r == 1:
                return True
            return False
        return False
    
    def sprawdz_czy_anagramy(self):
        if len(self.s1) != len(self.s2):
            return False
        s1_list = list(self.s1)
        s1_list.sort()
        s2_list = list(self.s2)
        s2_list.sort()
        return s1_list == s2_list

slowo = Slowa("kajak", "kajak")
slowo.wyswietl_wyrazy()
print(slowo.sprawdz_czy_palindrom())
print(slowo.sprawdz_czy_metagramy())
print(slowo.sprawdz_czy_anagramy())