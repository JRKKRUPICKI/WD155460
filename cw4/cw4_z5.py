import sys

class CiagArytmetyczny:

    a1 = 0
    r = 0
    n = 0

    def wyswietl_dane(self):
        print(f"a1={self.a1} r={self.r} n={self.n}")
    
    def pobierz_elemety(self):
        print("a1=")
        self.a1 = int(sys.stdin.readline())
        print("r=")
        self.r = int(sys.stdin.readline())
        print("n=")
        self.n = int(sys.stdin.readline())
    
    def pobierz_parametry(self):
        print("a1=")
        self.a1 = int(sys.stdin.readline())
        print("r=")
        self.r = int(sys.stdin.readline())
        print("n=")
        self.n = int(sys.stdin.readline())
    
    def policz_sume(self):
        return (2 * self.a1 + (self.n - 1) * self.r) / 2 * self.n
    
    def policz_elementy(self):
        return self.a1 + (self.n - 1) * self.r

ca = CiagArytmetyczny()
ca.pobierz_parametry()
ca.wyswietl_dane()
print(ca.policz_sume())
print(ca.policz_elementy())