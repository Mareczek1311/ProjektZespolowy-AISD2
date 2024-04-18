from file_reader import File_reader
from graham import Graham
from fordfulkerson import FordFulkerson

class Main:
    def __init__(self, filePath):
        self.fr = File_reader(filePath)
        self.data = {}
        self.punkty = []

    def getPunkty(self):
        return [key for key in self.data["adjList"]]

    def run(self):
        self.data = self.fr.read()

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
    m = Main('../data/przyklad3.txt')
    m.run()

if __name__ == '__main__':
    main()