import numpy as np
import matplotlib.pyplot as plt
import random

def rzucaj(n):
    wynik = []
    for i in range(n):
        wynik.append(random.randint(1,6) + random.randint(1,6))
    plt.hist(wynik, bins=2, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Suma rzutów')
    plt.ylabel('Prawdopodobieństwo')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

rzucaj(1000)
