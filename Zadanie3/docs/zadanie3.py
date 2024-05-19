import random

class Plaszczak:
    def __init__(self, numer, energia):
        """!
        # Konstruktor __init__:
            - Tworzy nowy obiekt płaszczaka i przyjmuje dwa argumenty\n
            - Przypisuje wartości "numer" i "energia" do odpowiednich atrytbutów obiektu
                @param numer - numer identyfikacyjny płaszczaka
                @param energia - wylosowana energia dla każdego z płaszczaków
        """
        self.numer = numer
        self.energia = energia
    
    def info_plaszczak(self):
        """!
        # Metoda info_plaszczak\n
            Wyświetla informacje o płaszczaku (numer, energia)
        """
        print(f"\tPlaszczak: {self.numer}, Energia: {self.energia}")

class Plot:
    """!
    # Konstruktor __init__:
        - Inicjalizuje pustą trasę patrolu.
        - Będzie tutaj przechowywana trasa strażnika.
    """
    def __init__(self):
        self.trasa = []

    def wygeneruj_plot(self, liczba_punktow, jasnosci):
        """!
        # Metoda wygeneruj_plot:
            - Generuje trasę patrolu na podstawie:\n
                @param "liczba_punktow" - liczba punktów w płocie w których strażnik musi się zatrzymać
                @param "jasnosci" - jasność punktu\n
            - Tworzy trasę patrolu na podstawie podanej liczby punktów i ich jasności.
        """
        if len(jasnosci) != liczba_punktow:
            print("Liczba wartości jasności musi być równa liczbie punktów.")
            return

        for i in range(1, liczba_punktow + 1):
            self.trasa.append((i, jasnosci[i - 1]))

        # pierwszy punkt jako ostatni
        self.trasa.append((self.trasa[0][0], self.trasa[0][1]))
    

    def wyswietl_plot(self):
        """!
        # Metoda wyswietl_plot:
            - Wyswietla trasę patrolu
            - Sprawdza, czy trasa nie jest pusta, a następnie wyświetla punkty trasy w czytelny sposób
        """
        if not self.trasa:
            print("Trasa jest pusta.")
            return
        
        print("Płot:")
        print(", ".join([f"({punkt},{jasnosc})" for punkt, jasnosc in self.trasa]))


    def patrol(self, plaszczaki, zasieg):
        """!
        # Metoda patrol
                @param plaszczaki - lista płaszczaków, którzy uczestniczą w patrolu
                @param zasieg - zasięg patrolu płaszczaka, czyli maksymalną odległość, jaką może przebyć pomiędzy punktami.
            
        - Dla każdego dnia patrolu, metoda wyświetla informacje o tym dniu oraz aktualną trasę patrolu.
        - Za pomocą metody znajdz_straznika znajduje płaszczaka z największą energią spośród dostępnych płaszczaków na liście plaszczaki.
        - Wywołuje metodę wyznacz_trase która wyznacza trasę dla znalezionego strażnika
            - Jeśli znaleziono strażnika, metoda przeprowadza jego patrolowanie.
            - Wyznaczana jest trasa patrolu dla strażnika, uwzględniając jego zasięg i dostępne punkty na trasie.
            - W trakcie patrolowania strażnik przemieszcza się po trasie, usuwając odwiedzone punkty i dodając je na koniec trasy, aby kontynuować cykl patrolowania.
        """
        dni = 7
        if zasieg == 0:
            print("Strażnik nie może przmieszczać się z zasięgiem 0")
            return
        
        for dzien in range(dni):
            print(f"Dzien: {dzien + 1}")
            self.wyswietl_plot()
            print()
            straznik = self.znajdz_straznika(plaszczaki)
            if straznik:
                print(f"Plaszczak z maks energia: Plaszczak:{straznik.numer}, energia: {straznik.energia}")
                print()
                self.wyznacz_trase(straznik, zasieg)
                print()
                plaszczaki.remove(straznik)
            else:
                print("Brak płaszczaków do patrolowania")
                break
            
            # usuwanie punktu z poczatku i dodawanie go na koniec kolejki
            self.trasa.pop(0)
            self.trasa.append(self.trasa[0])


    def znajdz_straznika(self, plaszczaki):
        """!
        # Metoda znajdz_straznika
        @param - plaszczaki - lista płaszczaków z której będziemy wybierać płaszczaka z największą energią
            
        - Iteruje po liście płaszczaków i porównuje ich energię.
        - Zmienna max_energia przechowuje dotychczasową maksymalną energię
        - Zmienna plaszczak_z_max_energia przechowuje referencję do płaszczaka z największą energią
        - Jeśli energia aktualnie przetwarzanego płaszczaka jest większa niż dotychczasowa maksymalna energia, wartość max_energia jest aktualizowana, a plaszczak_z_max_energia ustawiany jest na obecnie przetwarzanego płaszczaka.
        - Po przejrzeniu całej listy płaszczaków, zwracana jest referencja do płaszczaka z największą energią.
        - Jeśli lista jest pusta zwracana jest wartość None co oznacza brak płaszczaków
        """
        max_energia = 0
        plaszczak_z_max_energia = None

        for plaszczak in plaszczaki:
            if plaszczak.energia > max_energia:
                max_energia = plaszczak.energia
                plaszczak_z_max_energia = plaszczak

        return plaszczak_z_max_energia
    

    def wyznacz_trase(self, straznik, zasieg_straznika):
        """!
        # Metoda wyznacz_trase
        @param - straznik - obiekt klasy Plaszczak, który przeprowadza patrol
        @param - zasieg_straznika - maksymalna odległość, jaką strażnik może przebyć pomiędzy punktami
        
        - Jeśli znaleziono strażnika (czyli obiekt klasy Plaszczak), metoda patrol przeprowadza jego patrolowanie.
        - Wyznaczana jest trasa patrolu dla strażnika za pomocą metody wyznacz_trase. Proces ten obejmuje:
            - Inicjalizację pustej listy trasa_straznika, która będzie przechowywać kolejne punkty na trasie patrolu strażnika.
            - Ustalenie początkowego punktu startowego na trasie.
            - W pętli while, dopóki nie zostaną odwiedzone wszystkie punkty na trasie lub zasięg strażnika nie zostanie wyczerpany:
                        - Wybierane są dostępne punkty na trasie, które znajdują się w zasięgu strażnika.
                        - Jeśli punkt startowy jest dostępny, zostaje dodany na trasę patrolu.
                        - Wybierany jest kolejny punkt na trasie, który spełnia warunki:
                                - Jego jasność jest większa niż poprzedniego punktu na trasie (jeśli tak, punkt zostaje dodany na trasę jako "melodia").
                                - Jest to punkt o największym indeksie spośród dostępnych.
                        - Jeśli taki punkt zostaje znaleziony, dodaje się go na trasę patrolu i aktualizuje się indeks obecnego punktu.
                        - Proces ten kontynuuje się, dopóki możliwe są dalsze ruchy strażnika.
            - Po zakończeniu pętli, dodaje się punkt startowy na koniec trasy, aby strażnik mógł wrócić do punktu wyjściowego.
        - Po wyznaczeniu trasy, strażnik przeprowadza patrolowanie, przemieszczając się po trasie i kontrolując dostępne punkty.
        - Po zakończeniu patrolowania, strażnik zostaje usunięty z listy płaszczaków, aby uniknąć ponownego wyboru w następnych dniach patrolu.
        """
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

            # Sprawdzenie czy punkt startowy jest dostępny
            if punkt_startowy in dostepne_punkty and punkt_startowy not in trasa_straznika:
                trasa_straznika.append(punkt_startowy)
                break

            # Wybieranie punktu z dostępnych punktów
            wybrany_punkt = None
            for punkt in dostepne_punkty:
                if punkt not in trasa_straznika:
                    if punkt[1] < trasa_straznika[-1][1]:  # Jasnosc punktu mniejsza od obecnego punktu na trasie
                        if wybrany_punkt is None or punkt[0] > wybrany_punkt[0]:  # Największy indeks punktu
                            wybrany_punkt = punkt
                    elif punkt[1] > trasa_straznika[-1][1]:  # Jasnosc punktu większa od obecnego punktu na trasie
                        if wybrany_punkt is None or punkt[0] > wybrany_punkt[0]:  # Największy indeks punktu
                            wybrany_punkt = punkt

            if wybrany_punkt and wybrany_punkt not in trasa_straznika:
                if wybrany_punkt[1] > trasa_straznika[-1][1]:  # Jeśli jasność wybranego punktu jest większa
                    trasa_straznika.append("melodia")  # "melodia" do trasy
                trasa_straznika.append(wybrany_punkt)
                obecny_indeks = self.trasa.index(wybrany_punkt)
            else:
                break  # Jeśli nie ma odpowiedniego punktu przerwamy pętlę

            print("Dostępne punkty:", dostepne_punkty)
            print("Trasa strażnika:", trasa_straznika)
        
        trasa_straznika.append(punkt_startowy)
        print("Trasa strażnika:", trasa_straznika)

        return trasa_straznika

