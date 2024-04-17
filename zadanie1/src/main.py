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
        self.punkty = self.getPunkty()
        graham = Graham(self.punkty)
        print(graham.getOtoczka())
        graham.draw()

def main():
    m = Main('../data/przyklad2.txt')
    m.run()

if __name__ == '__main__':
    main()