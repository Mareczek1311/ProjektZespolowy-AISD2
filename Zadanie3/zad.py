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
    
    def wygeneruj_trase_straznika(self, punkt_orientacyjny, maks_punkt_zatrzymania):
        trasa = []
        punkt_startowy = punkt_orientacyjny[0]
        aktualny_punkt = punkt_startowy
        punkty_zatrzymania = 0

        while True:
            trasa.append(aktualny_punkt)
            punkty_zatrzymania += 1

            indeks = punkt_orientacyjny.index(aktualny_punkt)
            nastepny_indeks = (indeks + 1) % len(punkt_orientacyjny)
            nastepny_punkt = punkt_orientacyjny[nastepny_indeks]

            if nastepny_punkt > aktualny_punkt or punkty_zatrzymania > maks_punkt_zatrzymania:
                aktualny_punkt = nastepny_punkt
                punkty_zatrzymania = 0
            else:
                aktualny_punkt = punkt_orientacyjny[0]
                self.energia += 1

            if aktualny_punkt == punkt_startowy:
                break

        self.trasa = trasa

liczba_punktow = 10
jasnosci = [random.randint(1, 100) for _ in range(liczba_punktow)]
liczba_plaszczakow = 5
plaszczaki = [Plaszczak(i + 1, random.randint(1, 10)) for i in range(liczba_plaszczakow)]
maks_punkty_zatrzymania = 3

for plaszczak in plaszczaki:
    plaszczak.wygeneruj_trase_straznika(jasnosci, maks_punkty_zatrzymania)
    print(f"Straznik {plaszczak.numer}: Trasa: {plaszczak.trasa}, Energia: {plaszczak.energia}")

#plaszczak = Plaszczak(1, 10)
#jasnosci = [1, 2, 3, 4, 5]
#plaszczak.wygeneruj_plot(5, jasnosci)
#print(plaszczak.trasa)
