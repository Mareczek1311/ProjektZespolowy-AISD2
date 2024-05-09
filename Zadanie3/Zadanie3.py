import heapq

class Plaszczak:
    def __init__(self, numer, energia):
        self.numer = numer
        self.energia = energia

    def info_plaszczak(self):
        print(f"Plaszczak: {self.numer}, Energia: {self.energia}")

class Plot:
    def __init__(self):
        self.trasa = []

    def wygeneruj_plot(self, liczba_punktow, jasnosci):
        if len(jasnosci) != liczba_punktow:
            print("Liczba wartości jasności musi być równa liczbie punktów.")
            return

        for i in range(1, liczba_punktow + 1):
            self.trasa.append((i, jasnosci[i - 1]))

        # pierwszy punkt jako ostatni
        self.trasa.append((self.trasa[0][0], self.trasa[0][1]))

    def wyswietl_plot(self):
        if not self.trasa:
            print("Trasa jest pusta.")
            return

        for punkt, jasnosc in self.trasa:
            print(f"Punkt{punkt}, jasnosc {jasnosc}")

    def patrol(self, plaszczaki, dni, mozliwe_punkty):
        for dzien in range(dni):
            print(f"Dzien: {dzien + 1}")
            self.wyswietl_plot()
            print()
            straznik = self.znajdz_straznika(plaszczaki)
            if straznik:
                print(f"Plaszczak z maks energia: Plaszczak:{straznik.numer}")
                print()
                self.wyznacz_trase(straznik, mozliwe_punkty)
                print()
                plaszczaki.remove(straznik)
            else:
                print("Brak plaszczakow do patrolowania")
                break
            
            # usuwanie punktu z poczatku i dodawanie go na koniec kolejki
            self.trasa.pop(0)
            self.trasa.append(self.trasa[0])



    def znajdz_straznika(self, plaszczaki):
        max_energia = 0
        plaszczak_z_max_energia = None

        for plaszczak in plaszczaki:
            if plaszczak.energia > max_energia:
                max_energia = plaszczak.energia
                plaszczak_z_max_energia = plaszczak

        return plaszczak_z_max_energia

    def wyznacz_trase(self, straznik, zasieg_straznika):
        trasa_straznika = []
        obecny_indeks = 0
        punkt_startowy = self.trasa[0]

        while obecny_indeks < len(self.trasa) - 1:
            if self.trasa[obecny_indeks] not in trasa_straznika:
                trasa_straznika.append(self.trasa[obecny_indeks])
            dostepne_punkty = []

            for i in range(obecny_indeks + 1, min(obecny_indeks + zasieg_straznika + 1, len(self.trasa))):
                if self.trasa[i] not in trasa_straznika:
                    dostepne_punkty.append(self.trasa[i])

            if punkt_startowy in dostepne_punkty and punkt_startowy not in trasa_straznika:
                trasa_straznika.append(punkt_startowy)
                break

            wybrany_punkt = None
            for punkt in dostepne_punkty:
                if punkt not in trasa_straznika:
                    if punkt[1] < trasa_straznika[-1][1]:
                        if wybrany_punkt is None or punkt[0] > wybrany_punkt[0]:
                            wybrany_punkt = punkt
                    elif punkt[1] > trasa_straznika[-1][1]:
                        if wybrany_punkt is None or punkt[0] > wybrany_punkt[0]:
                            wybrany_punkt = punkt

            if wybrany_punkt and wybrany_punkt not in trasa_straznika:
                if wybrany_punkt[1] > trasa_straznika[-1][1]:
                    trasa_straznika.append("melodia")
                trasa_straznika.append(wybrany_punkt)
                obecny_indeks = self.trasa.index(wybrany_punkt)
            else:
                break
            print("Dostępne punkty:", dostepne_punkty)
            print("Trasa strażnika:", trasa_straznika)
        
        trasa_straznika.append(punkt_startowy)
        print("Trasa strażnika:", trasa_straznika)

        return trasa_straznika





# Testy

plaszczaki1 = [
    Plaszczak(1, 5),
    Plaszczak(2, 8),
    Plaszczak(3, 3),
    Plaszczak(4, 10),
    Plaszczak(5, 7),
    Plaszczak(6, 3),
    Plaszczak(7, 2)
]

jasnosci_punktow1 = [10, 9, 8, 9, 5]
plot1 = Plot()
plot1.wygeneruj_plot(5, jasnosci_punktow1)

plot1.patrol(plaszczaki1, 7, 2)

#print("\n\n====== TEST 2 ======\n")

plaszczaki2 = [
    Plaszczak(1, 5),
    Plaszczak(2, 8),
    Plaszczak(3, 3),
    Plaszczak(4, 10),
    Plaszczak(5, 7),
    Plaszczak(6, 3),
    Plaszczak(7, 2),
    Plaszczak(8, 2),
    Plaszczak(9, 2)
]

#jasnosci_punktow2 = [8, 9, 8, 7]
#plot2 = Plot()
#plot2.wygeneruj_plot(4, jasnosci_punktow2)

#plot2.patrol(plaszczaki2, 7, 2)

#plot1.wyswietl_plot()
