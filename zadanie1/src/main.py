import random

from file_reader import File_reader
from graham import Graham
from fordfulkerson import FordFulkerson
from random_tragarze import random_tragarze

def oblicz_odleglosc(p1, p2):
    #odleglosc dwoch punktow x1  y1 x2  y2
    odl = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    return odl


class Main:
    def __init__(self):
        self.fr = File_reader()
        self.data = {}
        self.punkty = []

    def getPunkty(self):
        return [key for key in self.data["adjList"]]

    def run(self):

        self.data = self.fr.readPoints('../data/graf1.txt')
        #Gragam
        self.punkty = self.getPunkty()
        print(self.punkty)

        bez_10 = self.punkty.copy()
        
        bez_10.remove((10, 0))

        graham = Graham(bez_10)
        print("Otoczka: ")
        print(graham.getOtoczka())
        graham.draw(graham.punkty, graham.getOtoczka())
        otoczka = graham.getOtoczka()

        odleglosci = []

        for i in range(1, len(otoczka)):
            odl = oblicz_odleglosc(otoczka[i-1], otoczka[i])
            odleglosci.append([otoczka[i-1], odl])
        
        print(odleglosci)
        
        for pkt in odleglosci:
            print(pkt)
            self.data["adjList"][pkt[0]][0] = ((10, 0), pkt[1])
        

        #tragarze
        #tragarze = self.fr.readTragarzy("../data/tragarze5.txt")
        tragarze = random_tragarze(10, '50/50')
        solver = FordFulkerson(len(tragarze), tragarze["start"], tragarze["end"], tragarze["punkty"])
        solver.config(tragarze["start"], tragarze["end"], tragarze["adjList"])
        print(solver.getMaxFlow())
        print("Graph:")
        solver.getGraph()
        solver.drawTragarze()

        #FordFulkerson
        n = len(self.punkty)
        solver = FordFulkerson(n, self.data["start"], self.data["end"], self.punkty)
        solver.config(self.data["start"], self.data["end"], self.data["adjList"])
        print(solver.getMaxFlow())
        print("Graph:")
        solver.getGraph()
        solver.draw_plan_budowy()

if __name__ == '__main__':
    m = Main()
    m.run()
