import random

class Plaszczak:
    def __init__(self, numer, energia):
        self.numer = numer
        self.energia = energia
        self.trasa = [] 

    def wygeneruj_plot(self, liczba_punktow, jasnosci):
        self.trasa = [random.choice(jasnosci) for _ in range(liczba_punktow)]

    # punkt_startowy - od ktorego zaczyna sie straznik
    # punkt_zatrzymania - miejsca w ktorych musi sie zatrzymac podczas trasy
    # aktualny_punkt - obecne miejsce tego barana


    #dokonczyc
    def wygeneruj_trase_straznika(punkt_orientacyjny, straznik, maks_punkt_zatrzymania):
        trasa = []
        punkt_startowy = punkt_orientacyjny[0]
        aktualny_punkt = punkt_startowy
        punkty_zatrzymania = 0

        while True:
            trasa.append(aktualny_punkt)
            punkty_zatrzymania += 1



plaszczak = Plaszczak(1, 10)
jasnosci = [1, 2, 3, 4, 5]
plaszczak.wygeneruj_plot(5, jasnosci)
print(plaszczak.trasa)
