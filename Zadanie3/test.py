import pytest
import random
from zad import Plaszczak, Plot

@pytest.fixture
def plaszczaki():
    return [
        Plaszczak(1, 5),
        Plaszczak(2, 8),
        Plaszczak(3, 3),
        Plaszczak(4, 10),
        Plaszczak(5, 7),
        Plaszczak(6, 4),
        Plaszczak(7, 1)
    ]

@pytest.fixture
def plot():
    return Plot()

def test_wygeneruj_plot(plot):
    # Testuje generowanie trasy
    jasnosci_punktow = [10, 9, 8, 5, 9, 8]
    plot.wygeneruj_plot(len(jasnosci_punktow), jasnosci_punktow)
    assert len(plot.trasa) == len(jasnosci_punktow) + 1  # Sprawdzamy czy liczba punktow na trasie zgadza sie

def test_znajdz_straznika_gdy_brak_plaszczakow(plot):
    # Sprawdzamy co sie dzieje gdy nie ma plaszczakow
    plaszczaki = []
    straznik = plot.znajdz_straznika(plaszczaki)
    assert straznik is None  # Sprawdzamy czy zwroci None jesli jest plaszczakow brak

def test_patrolowanie_z_brakiem_płaszczaków(plot):
    # Sprawdzamy czy trasa sie nie zmienia jesli brak plaszczakow
    plaszczaki = []
    zasieg_straznika = 2
    jasnosci_punktow = [10, 9, 8, 5, 9, 8]
    plot.wygeneruj_plot(len(jasnosci_punktow), jasnosci_punktow)
    plot.patrol(plaszczaki, zasieg_straznika)
    assert len(plot.trasa) == len(jasnosci_punktow) + 1

def test_znajdz_straznika(plaszczaki, plot):
    # Sprawdzamy czy funkcja znajduje poprawnie straznikow
    straznik = plot.znajdz_straznika(plaszczaki)
    assert straznik is not None  # Oczekujemy ze znajduje

def test_wyznacz_trase(plot, plaszczaki):
    # Sprawdzamy czy trasa straznika zostaje poprawnie wyznaczona (czy jest > 0)
    zasieg_straznika = 2
    jasnosci_punktow = [10, 9, 8, 5, 9, 8]
    plot.wygeneruj_plot(len(jasnosci_punktow), jasnosci_punktow)
    straznik = plot.znajdz_straznika(plaszczaki)
    trasa_straznika = plot.wyznacz_trase(straznik, zasieg_straznika)
    assert len(trasa_straznika) > 0

def test_patrolowanie_z_zasiegiem_0(plaszczaki, plot):
    # Sprawdzamy czy trasa nie zmieni sie gdy straznik ma zasieg 0 (oczekujemy ze bedzie niezmieniona)
    zasieg_straznika = 0
    jasnosci_punktow = [10, 9, 8, 5, 9, 8]
    plot.wygeneruj_plot(len(jasnosci_punktow), jasnosci_punktow)
    plot.patrol(plaszczaki, zasieg_straznika)
    assert len(plot.trasa) == len(jasnosci_punktow) + 1

def test_przemieszczenie_straznika_po_pierwszym_dniu(plot):
    # Sprawdzamy czy trasa pozostaje niezmieniona po pierwszym dniu patrolu (pierwszy i ostatni punkt na trasie beda takie same)
    plaszczaki = [
        Plaszczak(1, 5),
        Plaszczak(2, 8),
        Plaszczak(3, 3),
        Plaszczak(4, 10),
        Plaszczak(5, 7),
        Plaszczak(6, 4),
        Plaszczak(7, 1)
    ]
    zasieg_straznika = 2
    jasnosci_punktow = [10, 9, 8, 5, 9, 8]
    plot.wygeneruj_plot(len(jasnosci_punktow), jasnosci_punktow)
    plot.patrol(plaszczaki, zasieg_straznika)
    assert plot.trasa[0] == plot.trasa[-1]

def test_wyznacz_trase_z_zasiegiem_0(plot, plaszczaki):
    # Sprawdzam czy trasa straznika bedzie zawierala tylko punkt startowy poniewaz straznik ma zasieg = 0
    zasieg_straznika = 0
    jasnosci_punktow = [10, 9, 8, 5, 9, 8]
    plot.wygeneruj_plot(len(jasnosci_punktow), jasnosci_punktow)
    straznik = plot.znajdz_straznika(plaszczaki)
    trasa_straznika = plot.wyznacz_trase(straznik, zasieg_straznika)
    assert len(trasa_straznika) == 2  # Trasa bedzie skladac sie z punktu startowego i koncowego
    assert trasa_straznika[0] == trasa_straznika[-1]  # Sprawdzamy czy pierwszy i ostatni punkt sa takie same

def test_wyznacz_trase_dla_duzej_liczby_punktow(plot, plaszczaki):
    # Sprawdzamy dzialanie algorytmu wyznaczania trasy dla duzej liczby punktow
    liczba_punktow = 10000
    jasnosci_punktow = [random.randint(1, 10) for _ in range(liczba_punktow)]
    plot.wygeneruj_plot(liczba_punktow, jasnosci_punktow)
    straznik = plot.znajdz_straznika(plaszczaki)
    zasieg_straznika = 5
    trasa_straznika = plot.wyznacz_trase(straznik, zasieg_straznika)
    
    # Oczekujemy ze trasa straznika nie bedzie pusta oraz punkt startowy i koncowy musza byc takie same
    assert len(trasa_straznika) > 0
    assert trasa_straznika[0] == trasa_straznika[-1] 

def test_zuzywanie_wszystkich_plaszczakow(plot):
    # Sprawdzam czy wszyskie plaszczaki beda straznikami jesli maja ta sama energie
    plaszczaki = [
        Plaszczak(1, 5),
        Plaszczak(2, 5),
        Plaszczak(3, 5)
    ]
    zasieg_straznika = 2
    jasnosci_punktow = [10, 9, 8, 5, 9, 8]
    plot.wygeneruj_plot(len(jasnosci_punktow), jasnosci_punktow)
    plot.patrol(plaszczaki, zasieg_straznika)
    
    assert len(plaszczaki) == 0
