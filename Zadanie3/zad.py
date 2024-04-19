import random

class Plaszczak:
    def __init__(self, numer, energia):
        self.numer = numer
        self.energia = energia
        self.trasa = []

    def wygeneruj_plot(self, liczba_punktow, jasnosci):
        self.trasa = [random.choice(jasnosci) for _ in range(liczba_punktow)]

plaszczak = Plaszczak(1, 10)
jasnosci = [1, 2, 3, 4, 5]
plaszczak.wygeneruj_plot(5, jasnosci)
print(plaszczak.trasa)
