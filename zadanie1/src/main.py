import random

from file_reader import File_reader
from graham import Graham
from fordfulkerson import FordFulkerson
from tragarz import Tragarz
from Klub import Klub
from draw_graph import draw_tragarze

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
        ilosc_tragarzy = random.randint(6, 10)
        tragarze = {}

        indexYlewy = 0
        indexYprawy = 0

        for i in range(ilosc_tragarzy):
            klub = random.randint(0, n_klubow-1)
            rece = random.choice([True, False])
            if rece:
                indexYlewy += 1
                tragarze[Tragarz(i, klub, rece, indexYlewy)] = []
            else:
                indexYprawy += 1
                tragarze[Tragarz(i, klub, rece, indexYprawy)] = []

        return tragarze

    def utworzRelacjeTragarzy(self, tragarze, kluby):
        for t1 in tragarze:
            for t2 in tragarze:
                if t1 != t2 and t1.rece_z_przodu != t2.rece_z_przodu and (t1.id_ulubionego_klubu == t2.id_ulubionego_klubu or kluby[t1.id_ulubionego_klubu].sprawdzRelacje(t2.id_ulubionego_klubu)):
                    tragarze[t1].append((t2, 1))

        return tragarze

    def czescPierwsza(self):
        #Kluby
        kluby = self.fr.readKluby(self.fileKluby)
        kluby = self.fr.readKlubyRelacje(self.fileKlubyRelacje, kluby)

        #Tragarze
        tragarze = self.generujTragarzy(len(kluby))
        tragarze = self.utworzRelacjeTragarzy(tragarze, kluby)

        tragarzStart = Tragarz(len(tragarze), 0, True, 0, 1)
        tragarzEnd = Tragarz(len(tragarze)+1, 1, False, 0, 7)
        tragarze[tragarzStart] = []

        for tragarz in tragarze:
            if  tragarz.rece_z_przodu and tragarz != tragarzStart:
                tragarze[tragarzStart].append((tragarz, 1))

        tragarze[tragarzEnd] = []
        for tragarz in tragarze:
            if not tragarz.rece_z_przodu and tragarz != tragarzEnd:
                tragarze[tragarz].append((tragarzEnd, 1))

        kluczeTragarze = [key for key in tragarze]
        print("Tragarze: ")
        print(kluczeTragarze)

        solver = FordFulkerson(len(tragarze), tragarzStart, tragarzEnd, kluczeTragarze)

        solver.config(tragarzStart, tragarzEnd, tragarze)
        print(solver.getMaxFlow())
        print("Graph:")
        solver.getGraph()

        draw_tragarze(tragarze, kluby)


    def run(self):

        self.czescPierwsza()

        return
        self.data = self.fr.readPoints(self.filePunkty)

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