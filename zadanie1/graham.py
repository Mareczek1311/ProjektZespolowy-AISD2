import networkx as nx
import matplotlib.pyplot as plt


###powinny byc z pliku ladowane i powinien robic to inny program !DO POPRAWIENIA!
dane = [
    (1, 2),
    (3, 4),
    (4, 3),
    (5, 4),
    (4, 5),
    (2, 6),
    (1, 4),
    (2, 4),
    (3, 3),
    (5, 5),
    (6, 6),
]

class Gragam:
    def __init__(self, punkty) -> None:
        self.calculated = False
        self.punkty = punkty
        self.convexHull = []

    def findMin(self, punkty):
        min = punkty[0]

        for i in range(1, len(punkty)):
            if punkty[i][1] < min[1]:
                min = punkty[i]
            elif punkty[i][1] == min[1]:
                if punkty[i][0] < min[0]:
                    min = punkty[i]
        return min

    #wyznacznik
    def det(self, p1, p2, p3):
        return p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1]

    def algorytm(self):
        punkty = self.punkty
        min = self.findMin(punkty)

        ###bubble sort (n^2) zla zlozonosc !DO POPRAWIENIA!
        for i in range(1, len(punkty)):
            for j in range(i+1, len(punkty)):
                wyz = self.det(min, punkty[i], punkty[j])
                if wyz < 0:
                    punkty[i], punkty[j] = punkty[j], punkty[i]
                if wyz == 0:
                    if punkty[i][0] < punkty[j][0]:
                        punkty[i], punkty[j] = punkty[j], punkty[i]

        stack = []
        stack.append(min)
        stack.append(punkty[1])
        stack.append(punkty[2])

        #grahamka ;)
        for i in range(3, len(punkty)):
            while self.det(stack[-2], stack[-1], punkty[i]) < 0:
                stack.pop()
            stack.append(punkty[i])
        stack.append(min)
        
        self.convexHull = stack
    
    def draw(self):
        if not self.calculated:
            self.algorytm()
            self.calculated = True

        G = nx.DiGraph()

        G.add_nodes_from([point for point in self.punkty])
        G.add_edges_from([(self.convexHull[i], self.convexHull[i+1]) for i in range(len(self.convexHull)-1)])
        pos = {node: node for node in G.nodes()}

        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")

        plt.axhline(y=0, color='k', linestyle='-', linewidth=1)
        plt.axvline(x=0, color='k', linestyle='-', linewidth=1)

        plt.grid(True)
        plt.show()
    
    def getOtoczka(self):
        if not self.calculated:
            self.algorytm()
            self.calculated = True
        
        return self.convexHull



#Przykladowe urzycie

g = Gragam(dane)

print(g.getOtoczka())

g.draw()
