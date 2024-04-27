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

    def wyswietl_plot(self):
        if not self.trasa:
            print("Trasa jest pusta.")
            return

        for punkt, jasnosc in self.trasa:
            print(f"Punkt{punkt}, jasnosc {jasnosc}")

    def patrol(self, plaszczaki, dni):
        for dzien in range(dni):
            print()
            print(f"Dzień: {dzien + 1}")
            print()
            straznik = self.znajdz_straznika(plaszczaki)
            if straznik:
                print(f"Plaszczak z maks energia: {straznik.numer}")
            else:
                print("Brak plaszczaków do patrolowania.")
                break

            punkt_start = 1
            for index, (punkt, jasnosc) in enumerate(self.trasa):
                if index == len(self.trasa) - 1:
                    # Jeśli to ostatni punkt, strażnik wraca do punktu startowego
                    if straznik:
                        print(f"Plaszczak {straznik.numer} wrócił do punktu {punkt_start}.")
                    break

                if index < len(self.trasa) - 1:
                    nastepna_jasnosc = self.trasa[index + 1][1]
                    if jasnosc < nastepna_jasnosc:
                        print("Plaszczak musi odpoczac ==== Melodia")
                        plaszczaki.remove(straznik)
                        straznik = self.znajdz_straznika(plaszczaki)
                        if not straznik:
                            print("Brak plaszczaków do patrolowania.")
                            break
                    if straznik:
                        print(f"Plaszczak {straznik.numer} patroluje punkt: {punkt}")
                    punkt_start = punkt

        print()

    def znajdz_straznika(self, plaszczaki):
        max_energia = 0
        plaszczak_z_max_energia = None
        
        for plaszczak in plaszczaki:
            if plaszczak.energia > max_energia:
                max_energia = plaszczak.energia
                plaszczak_z_max_energia = plaszczak
                
        return plaszczak_z_max_energia


plaszczaki = [
    Plaszczak(1, 5),
    Plaszczak(2, 8),
    Plaszczak(3, 3),
    Plaszczak(4, 10),
    Plaszczak(5, 7),
    Plaszczak(6, 3),
    Plaszczak(7, 2)
]

jasnosci_punktow = [3, 5, 2, 8, 1, 6, 4, 9, 7, 2]
plot1 = Plot()
plot1.wygeneruj_plot(10, jasnosci_punktow)

plot1.patrol(plaszczaki, 7)
