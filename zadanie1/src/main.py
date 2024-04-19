import random

from file_reader import File_reader
from graham import Graham
from fordfulkerson import FordFulkerson
from tragarz import Tragarz
from Klub import Klub

class Main:
    def __init__(self, filePunkty, fileKluby, fileKlubyRelacje):
        self.fr = File_reader()
        self.data = {}
        self.punkty = []
        self.filePunkty = filePunkty
        self.fileKluby = fileKluby
        self.fileKlubyRelacje = fileKlubyRelacje

    def getPunkty(self):
        return [key for key in self.data["adjList"]]

    def generujTragarzy(self, n_klubow):
        ilosc_tragarzy = random.randint(6, 20)
        tragarze = []
        for _ in range(ilosc_tragarzy):
            klub = random.randint(0, n_klubow-1)
            rece = random.choice([True, False])
            tragarze.append(Tragarz(klub, rece))
        
        return tragarze

    def run(self):

        #Kluby
        kluby = self.fr.readKluby(self.fileKluby)
        kluby = self.fr.readKlubyRelacje(self.fileKlubyRelacje, kluby)

        #Tragarze
        tragarze = self.generujTragarzy(len(kluby))
        
        print("Tragarze:")
        for t in tragarze:
            print(t)


        return
        self.data = self.fr.read(self.filePunkty)

        #Gragam
        self.punkty = self.getPunkty()
        graham = Graham(self.punkty)
        print("Otoczka: ")
        print(graham.getOtoczka())
        graham.draw()


        #FordFulkerson
        n = len(self.punkty)
        solver = FordFulkerson(n, self.data["start"], self.data["end"], self.punkty)
        solver.config(self.data["start"], self.data["end"], self.data["adjList"])
        print(solver.getMaxFlow())
        print("Graph:")
        solver.getGraph()
        solver.draw()

        

def main():
    m = Main('../data/przyklad3.txt', '../data/kluby.txt', '../data/kluby_relacje.txt')
    m.run()

if __name__ == '__main__':
    main()