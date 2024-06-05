# **Zadanie 3**

## Opis działania
- Program działa w następujący sposób
  - tworzymy tablicę 7 płaszczaków oraz losujemy ich energię z przedziału (1,10)
  - ustalamy jasności punktów oraz generujemy płot z tymi jasnościami (każdy punkt ma swoją jasność)
  - określamy zasięg strażnika tzn. strażnik będzie przechodził do punktów które są w jego zasięgu
  - patrol rozpoczynamy od wyszukania strażnika, który ma największą energie.
  - każdy strażnik patroluje jeden dzień, strażnik porusza sie wokół płotu po punktach, (gdy przechodzi do punktu o większej jasności to musi odpocząć = 'melodia' , a jeśli do mniejszej to nie musi)
  - następnego dnia, następny strażnik rozpocznie swój patrol jeden punkt dalej niż poprzedni strażnik
  - program działa do momentu odbycia 7-dniowego patrolu
    
## Przykładowe dane wejściowe

- zasieg straznika = 3;
- plaszczaki1 = [Plaszczak(i, random.randint(1, 10)) for i in range(1, 8)]
- jasnosci_punktow = [10, 9, 8, 9, 5]
- plot1 = Plot()
- plot1.wygeneruj_plot(len(jasnosci_punktow1), jasnosci_punktow1)
- plot1.patrol(plaszczaki1, zasieg_straznika1)

## Przykładowe dane wyjściowe dla pierwszego i drugiego dnia
## Dzien: 1
 - Płot: (1,10), (2,9), (3,8), (4,9), (5,5), (1,10)

 - Plaszczak z maks energia: Plaszczak:4, energia: 8

 - Dostępne punkty: [(2, 9), (3, 8), (4, 9)]
 - Trasa strażnika: [(1, 10), (4, 9)]
 - Dostępne punkty: [(5, 5)]
 - Trasa strażnika: [(1, 10), (4, 9), (5, 5)]
 - Trasa strażnika: [(1, 10), (4, 9), (5, 5), (1, 10)]

## Dzien: 2
 - Płot: (2,9), (3,8), (4,9), (5,5), (1,10), (2,9)

 - Plaszczak z maks energia: Plaszczak:6, energia: 8

 - Dostępne punkty: [(3, 8), (4, 9), (5, 5)]
 - Trasa strażnika: [(2, 9), (5, 5)]
 - Dostępne punkty: [(1, 10)]
 - Trasa strażnika: [(2, 9), (5, 5), 'melodia', (1, 10)]
 - Trasa strażnika: [(2, 9), (5, 5), 'melodia', (1, 10), (2, 9)]
  

