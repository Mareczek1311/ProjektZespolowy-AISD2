import random

from file_reader import File_reader
from graham import Graham
from fordfulkerson import FordFulkerson

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

    def run(self):

        self.data = self.fr.readPoints(self.filePunkty)

        #Gragam
        self.punkty = self.getPunkty()
        graham = Graham(self.punkty)
        print("Otoczka: ")
        print(graham.getOtoczka())
        graham.draw()

        #tragarze
        tragarze = self.fr.readTragarzy("../data/kluby_przyklad1.txt")
        solver = FordFulkerson(len(tragarze), tragarze["start"], tragarze["end"], tragarze["punkty"])
        solver.config(tragarze["start"], tragarze["end"], tragarze["adjList"])
        print(solver.getMaxFlow())
        print("Graph:")
        solver.getGraph()
        solver.draw()

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