from graham import Graham
from fordfulkerson import FordFulkerson
from random_points import randomPoints
from random_tragarze import random_tragarze
import time

import networkx as nx
import matplotlib.pyplot as plt

def testowanie_graham():
    ilosc = 100
    statystyki = []
    for i in range(1, 40):
        print("TEST NR: ", i, " DLA ILOSCI: ", ilosc)
        start_time = time.time()

        punkty = randomPoints(ilosc)
        g = Graham(punkty)
        statystyki.append([ilosc, time.time() - start_time])

        ilosc += 100
        print("-- DLA ILOSCI: ", ilosc, " CZAS WYKONANIA: ", time.time() - start_time)

    draw_statystyki_graham(statystyki)

def testowanie_fordfulkerson_tragarze(option='default'):
    ilosc = 100
    statystyki = []
    for i in range(1, 20):
        print("TEST NR: ", i, " DLA ILOSCI: ", ilosc)
        start_time = time.time()

        tragarze = random_tragarze(ilosc, option)
        solver = FordFulkerson(len(tragarze), tragarze["start"], tragarze["end"], tragarze["punkty"])
        solver.config(tragarze["start"], tragarze["end"], tragarze["adjList"])
        
        if option == 'default':
            statystyki.append([ilosc, time.time() - start_time, ilosc//2])
        elif option == '50/50':
            statystyki.append([ilosc, time.time() - start_time, ilosc//4])

        ilosc += 100
        print("-- DLA ILOSCI: ", ilosc, " CZAS WYKONANIA: ", time.time() - start_time)

    draw_statystyki_fordfulkerson(statystyki)

def draw_statystyki_graham(statystyki):
    x = [i[0] for i in statystyki]
    y = [i[1] for i in statystyki]

    plt.plot(x, y)
    plt.xlabel('Ilosc punktow')
    plt.ylabel('Czas wykonania')
    plt.show()

def draw_statystyki_fordfulkerson(statystyki):
    # x to ilosc punktow 
    # y to czas wykonania
    # wielkosc node to ilosc krawedzi
    x = [i[0] for i in statystyki]
    y = [i[1] for i in statystyki]
    size = [i[2] for i in statystyki]

    plt.scatter(x, y, s=size)
    plt.xlabel('Ilosc punktow')
    plt.ylabel('Czas wykonania')
    plt.show()

if __name__ == "__main__":
    testowanie_graham()
    testowanie_fordfulkerson_tragarze()
    testowanie_fordfulkerson_tragarze(option='50/50')
