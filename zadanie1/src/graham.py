import networkx as nx
import matplotlib.pyplot as plt
from functools import cmp_to_key

## Klasa ktora pozowli na wyznaczenie otoczki wypuklej
class Graham: 

    def __init__(self, punkty = []) -> None: 
        """!
        Konstruktor dla klasy Graham
        @param punkty - lista punktow (x, y) dla ktorych chcemy wyznaczyc otoczke wypukla

        """

        self.calculated = False 
        self.punkty = punkty 
        self.convexHull = [] 
        self.min = None 

    def findMin(self, punkty):
        """!
        findMin Metoda ktora znajduje punkt o najmniejszej wspolrzednej y

        @param punkty - lista punktow (x, y) dla ktorych chcemy znalezc punkt o najmniejszej wspolrzednej y, kiedy sa takie same to wybieramy ten o wiekszej wspolrzednej x


        @return punkt (x, y) o najmniejszej wspolrzednej y a jezeli jest takich kilka to o wiekszej wspolrzednej x
        """
        min = punkty[0]

        for i in range(1, len(punkty)):
            if punkty[i][1] < min[1]:
                min = punkty[i]
            elif punkty[i][1] == min[1]:
                if punkty[i][0] > min[0]:
                    min = punkty[i]
        
        return min

    def det(self, p1, p2, p3):
        """!
        det Metoda ktora oblicza wyznacznik macierzy 2x2
        @param p1 - pierwszy punkt (x, y)
        @param p2 - drugi punkt (x, y)
        @param p3 - trzeci punkt (x, y)
        @return wyznacznik macierzy 3x3
        """
        return p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1]

    def distSq(self, p1, p2):
        """!
        distSq Metoda ktora oblicza kwadrat odleglosci miedzy dwoma punktami
        @param p1 - pierwszy punkt (x, y)
        @param p2 - drugi punkt (x, y)
        @return kwadrat odleglosci miedzy dwoma punktami
        """


        return ((p1[0] - p2[0]) * (p1[0] - p2[0]) +
                (p1[1] - p2[1]) * (p1[1] - p2[1]))

    def compare(self, p1, p2):
        """!
        compare Metoda ktora porownuje dwa punkty wzgledem punktu o najmniejszej wspolrzednej y
        @param p1 - pierwszy punkt (x, y)
        @param p2 - drugi punkt (x, y)
        @return -1 jezeli p1 jest mniejszy od p2, 1 jezeli p1 jest wiekszy od p2, 0 jezeli sa rowne
        """

        wyz = self.det(self.min, p1, p2)
        
        if wyz == 0:
            if self.distSq(self.min, p2) >= self.distSq(self.min, p1):
                return -1
            else:
                return 1
        else:
            if wyz > 0:
                return -1
            else:
                return 1

    def algorytm(self):
        """!
        algorytm Metoda ktora wyznacza otoczke wypukla dla punktow z listy punkty
        
        """

        punkty = self.punkty

        if len(punkty) < 3:
            self.convexHull = []
            return

        self.min = self.findMin(punkty)
        
        punkty = sorted(punkty, key=cmp_to_key(self.compare))


        stack = []
        stack.append(punkty[0])
        stack.append(punkty[1])
        stack.append(punkty[2])

        #grahamka ;)
        for i in range(3, len(punkty)):
            while self.det(stack[-2], stack[-1], punkty[i]) < 0:
                stack.pop()
            stack.append(punkty[i])
        
        self.convexHull = stack
    

    ## Metoda ktora rysuje otoczke wypukla
    def draw(self, punkty = [], otoczka = []):
        G = nx.DiGraph()

        otoczka.append(otoczka[0])

        G.add_nodes_from([point for point in punkty])
        G.add_edges_from([(otoczka[i], self.convexHull[i+1]) for i in range(len(otoczka)-1)])
        pos = {node: node for node in G.nodes()}

        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")

        plt.grid(True)
        plt.show()
    

    ## Metoda ktora zwraca otoczke wypukla
    def getOtoczka(self):
        if not self.calculated:
            self.algorytm()
            self.calculated = True
        
        return self.convexHull
