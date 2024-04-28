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
                print()
            else:
                print("Brak plaszczaków do patrolowania.")
                break
            ostatni_punkt = self.trasa[-1][0]  # Pobranie numeru ostatniego punktu
            for index, (punkt, jasnosc) in enumerate(self.trasa):
                if index < len(self.trasa) - 1:
                    nastepna_jasnosc = self.trasa[index + 1][1]
                    if jasnosc < nastepna_jasnosc:
                        print()
                        print(f"Plaszczak {straznik.numer} patroluje punkt: {punkt} Jasnosc - {jasnosc}")
                        print(f"Plaszczak {straznik.numer} musi odpoczac ==== Melodia ==== Punkt - {punkt}, Jasnosc - {jasnosc}")
                        print()
                        plaszczaki.remove(straznik)
                        straznik = self.znajdz_straznika(plaszczaki)
                        if not straznik:
                            print("Brak plaszczaków do patrolowania.")
                            break
                    if straznik:
                        print(f"Plaszczak {straznik.numer} patroluje punkt: {punkt} Jasnosc - {jasnosc}")
                    punkt_start = punkt

            # Po zakończeniu pętli wyświetlamy informację o powrocie do rzeczywistego ostatniego punktu trasy
            if straznik:
                print(f"Plaszczak {straznik.numer} wrócił do punktu {ostatni_punkt} Jasnosc - {jasnosc}")
                print("Koniec patrolu")

        print()

    def znajdz_straznika(self, plaszczaki):
        max_energia = 0
        plaszczak_z_max_energia = None
        
        for plaszczak in plaszczaki:
            if plaszczak.energia > max_energia:
                max_energia = plaszczak.energia
                plaszczak_z_max_energia = plaszczak
                
        return plaszczak_z_max_energia


plaszczaki1 = [
    Plaszczak(1, 5),
    Plaszczak(2, 8),
    Plaszczak(3, 3),
    Plaszczak(4, 10),
    Plaszczak(5, 7),
    Plaszczak(6, 3),
    Plaszczak(7, 2)
]

# Test 1 - zabraknie plaszczakow do patrolowania poniewaz nastepne punkty maja zbyt duze jasnosci niz poprzednie
jasnosci_punktow1 = [10, 9, 8, 9, 5, 4, 3, 2, 1, 0]
plot1 = Plot()
plot1.wygeneruj_plot(10, jasnosci_punktow1)

plot1.patrol(plaszczaki1, 7)

# Test 2 - nie zabraknie plaszczakow do patrolowania
print()
print()
print("====== TEST 2 ======")

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

jasnosci_punktow2 = [8, 9, 8, 7]
plot2 = Plot()
plot2.wygeneruj_plot(4, jasnosci_punktow2)

plot2.patrol(plaszczaki2, 7)


