import networkx as nx
import matplotlib.pyplot as plt

## Klasa reprezentujaca krawedz w grafie
class Edge:

    def __init__(self, fr, to, capacity, flow=0):
        """!
        Konstruktor klasy Edge.

        Inicjalizuje nową krawędź w grafie przepływowym, ustawiając wierzchołek początkowy, wierzchołek końcowy, pojemność krawędzi i przepływ przez krawędź.

        @param fr Wierzchołek początkowy.
        @param to Wierzchołek końcowy.
        @param capacity Pojemność krawędzi.
        @param flow Przepływ przez krawędź (domyślnie 0).
        """
        self.fr = fr
        self.to = to
        self.capacity = capacity #constant
        self.flow = flow
    
    def isResidual(self):
        """!
        Metoda, która sprawdza, czy krawędź jest krawędzią rezydualną.

        Krawędź rezydualna to taka, która ma zerową pojemność (`self.capacity`).

        @return True, jeżeli krawędź jest krawędzią rezydualną, False w przeciwnym wypadku.
        """
        return self.capacity == 0
    
    def remainingCapacity(self):
        """!
        Metoda, która zwraca pozostałą pojemność krawędzi.

        Pozostała pojemność krawędzi jest różnicą między jej całkowitą pojemnością (`self.capacity`) a aktualnym przepływem (`self.flow`).

        @return Pozostała pojemność krawędzi.
        """
        return self.capacity - self.flow

    def augment(self, newFlow):
        """!
        Metoda, która zwiększa przepływ przez krawędź w grafie przepływowym.

        Metoda aktualizuje przepływ przez krawędź, dodając nowy przepływ `newFlow` do bieżącego przepływu (`self.flow`),
        a jednocześnie odejmuje ten nowy przepływ od przepływu w krawędzi odwrotnej (`self.reverse.flow`).

        @param newFlow Ilość nowego przepływu, który ma zostać dodany do krawędzi.
        @return Brak zwracanej wartości. Metoda aktualizuje wewnętrzny stan krawędzi.
        """
        self.flow += newFlow
        self.reverse.flow -= newFlow


## Klasa implementująca algorytm Forda-Fulkersona
class FordFulkerson:
    def __init__(self, n, s, t, punkty):
        """!
        Konstruktor klasy FordFulkerson.

        Inicjalizuje nowy obiekt algorytmu Forda-Fulkersona z daną liczbą wierzchołków, wierzchołkiem startowym, wierzchołkiem końcowym
        oraz listą punktów reprezentujących wierzchołki w grafie.

        @param n Liczba wierzchołków w grafie.
        @param s Wierzchołek startowy.
        @param t Wierzchołek końcowy.
        @param punkty Lista punktów (x, y) reprezentujących wierzchołki w grafie.
        """
        self.inf = float("inf")
        self.n = n
        self.s = s
        self.t = t
        self.graph = {}
        self.visited = []
        self.visitedToken = 1
        self.maxFlow = 0
        self.solved = False
        self.punkty = punkty

    def addEdge(self, fr, to, capacity):
        """!
        Metoda ktora dodaje krawedz do grafu

        @param fr - wierzcholek poczatkowy
        @param to - wierzcholek koncowy
        @param capacity - pojemnosc krawedzi
        """

        if capacity <= 0:
            raise ValueError("Forward edge capacity <= 0")

        forward = Edge(fr, to, capacity)
        reverse = Edge(to, fr, 0)
        forward.reverse = reverse
        reverse.reverse = forward

        if fr not in self.graph:
            self.graph[fr] = []
        self.graph[fr].append(forward)
        
        if to not in self.graph:
            self.graph[to] = []
        self.graph[to].append(reverse)        

    def getGraph(self):
        """!
        Metoda ktora rysuje oraz zwraca graf
        @return graf
        """
        self.execute()
        for node in self.graph:
            print(node)
            for edge in self.graph[node]:
                print("  ->", edge.to, " Capacity: ", edge.capacity, " Flow: ", edge.flow) 

        return self.graph    

    def getMaxFlow(self):
        """!
        Metoda ktora zwraca maksymalny przeplyw w grafie
        @return maksymalny przeplyw w grafie
        """
        self.execute()
        return self.maxFlow
    
    def execute(self):
        """!
        Metoda ktora wywoluje algorytm Forda-Fulkersona jesli nie zostal jeszcze wywolany
        """ 
        if self.solved:
            return
        self.solved = True
        self.solve()
    
    def solve(self):
        """!
        Metoda, która rozwiązuje problem maksymalnego przepływu w grafie.

        Metoda implementuje algorytm Forda-Fulkersona, wykorzystując wyszukiwanie w głąb (DFS) do znalezienia ścieżek powiększających.
        Algorytm działa w pętli, dopóki możliwe jest znalezienie ścieżki powiększającej, zwiększając całkowity przepływ o przepustowość tej ścieżki.

        Złożoność czasowa:
        - W najgorszym przypadku: O(E * f), gdzie E to liczba krawędzi, a f to maksymalny przepływ w sieci.

        Złożoność pamięciowa:
        - Przechowywanie grafu i struktur pomocniczych: O(V + E), gdzie V to liczba wierzchołków, a E to liczba krawędzi.
        
        @return Brak zwracanej wartości. Wynikowy maksymalny przepływ jest przechowywany w atrybucie self.maxFlow.
        """
        f = 1
        
        while(f != 0):
            f = self.dfs(self.s, float("inf"))
            self.visited = []
            self.maxFlow += f

    def dfs(self, node, flow):
        """!
        Metoda ktora przeszukuje graf w glab

        @param node - wierzcholek
        @param flow - przeplyw
        @return przeplyw
        """
        if(node == self.t):
            return flow

        self.visited.append(node)

        edges = self.graph[node]

        for edge in edges:
            if edge.remainingCapacity() > 0 and edge.to not in self.visited:
                bottleNeck = self.dfs(edge.to, min(flow, edge.remainingCapacity()))

                if bottleNeck > 0:
                    edge.augment(bottleNeck)
                    return bottleNeck

        return 0

    def config(self, s, t, adjList):
        """!
        Metoda ktora konfiguruje graf

        @param s - wierzcholek startowy
        @param t - wierzcholek koncowy
        @param adjList - lista sasiedztwa
        """
        self.s = s
        self.t = t

        for node in adjList:
            for edge in adjList[node]:
                self.addEdge(node, edge[0], edge[1])

    def draw_plan_budowy(self):
        """!
        Metoda ktora rysuje graf 2
        """
        
        G = nx.DiGraph()

        point = []


        for i in range(len(self.punkty)):
            if self.punkty[i] != (10, 0):
                point.append((self.punkty[i][0], self.punkty[i][1]))
        print(point)
        G.add_nodes_from(point)
        labels = {}
        for node in self.graph:
            for edge in self.graph[node]:
                if edge.to != (10, 0) and edge.fr != (10, 0):
                    G.add_edge(node, edge.to, capacity=edge.capacity, flow=edge.flow)
                elif edge.to == (10, 0):
                    labels[node] = str(edge.flow) + "/" + str(edge.capacity)

        pos = {}
        for i in range(len(self.punkty)):
            if self.punkty[i] != (10, 0):
                pos[(self.punkty[i][0], self.punkty[i][1])] = (self.punkty[i][0], self.punkty[i][1])

        edge_labels = {}
        edge_labels_residual = {}
        
        for node in G.nodes():
            for edge in G.edges(node, data=True):
                if edge[2]['capacity'] != 0 and edge[1] != (10, 0):
                    edge_labels[(edge[0], edge[1])] = str(edge[2]['flow']) + "/" + str(edge[2]['capacity'])
                elif edge[1] != (10, 0):
                    edge_labels_residual[(edge[0], edge[1])] = edge[2]['flow']

        
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, labels=labels) 

        nx.draw_networkx_edge_labels(G, pos, bbox=None, edge_labels=edge_labels_residual, verticalalignment="top",  horizontalalignment ="right", font_size=6, font_color='red')

        nx.draw_networkx_edge_labels(G, pos, bbox=None, edge_labels=edge_labels, verticalalignment="bottom",   horizontalalignment ="left", font_size=6)
        plt.show()
        
    def draw(self):
        """!
        Metoda ktora rysuje graf
        """
        
        G = nx.DiGraph()

        point = []

        for i in range(len(self.punkty)):
            point.append((self.punkty[i][0], self.punkty[i][1]))

        G.add_nodes_from(point)
        for node in self.graph:
            for edge in self.graph[node]:
                
                G.add_edge(node, edge.to, capacity=edge.capacity, flow=edge.flow)

        pos = {node: node for node in G.nodes()}
        edge_labels = {}
        edge_labels_residual = {}
        
        labels = {}
        for node in G.nodes():
            for edge in G.edges(node, data=True):
                if edge[2]['capacity'] != 0:
                    edge_labels[(edge[0], edge[1])] = str(edge[2]['flow']) + "/" + str(edge[2]['capacity'])
                    if(edge[1] == (10, 0)):
                        labels[edge[0]] = str(edge[0][0]) + ", " + str(edge[0][1]) + " || " + str(edge[2]['flow']) + "/" + str(edge[2]['capacity'])
                    else:
                        labels[edge[0]] = str(edge[0][0]) + ", " + str(edge[0][1])
                else:
                    edge_labels_residual[(edge[0], edge[1])] = edge[2]['flow']


        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, labels=labels) 

        nx.draw_networkx_edge_labels(G, pos, bbox=None, edge_labels=edge_labels_residual, verticalalignment="top",  horizontalalignment ="right", font_size=6, font_color='red')

        nx.draw_networkx_edge_labels(G, pos, bbox=None, edge_labels=edge_labels, verticalalignment="bottom",   horizontalalignment ="left", font_size=6)
        plt.show()

    def drawTragarze(self):
        """!
        Metoda ktora rysuje graf
        """
        
        G = nx.DiGraph()

        point = []

        for i in range(len(self.punkty)):
            if self.punkty[i] != (0, 0) and self.punkty[i] != (6, 0):
                point.append((self.punkty[i][0], self.punkty[i][1]))

        G.add_nodes_from(point)
        for node in self.graph:
            for edge in self.graph[node]:
                if edge.isResidual() == False and edge.fr != (0, 0) and edge.to != (6, 0):
                    G.add_edge(node, edge.to, capacity=edge.capacity, flow=edge.flow)

        pos = {node: node for node in G.nodes()}
        edge_colors = []  # Domyślnie wszystkie krawędzie na czarno

        #jezeli przeplyw krawedzi jest > 0 to kolorujemy na czerwono
        for node in G.nodes():
            for edge in G.edges(node, data=True):
                if edge[2]['flow'] > 0:
                    edge_colors.append('red')
                else:
                    edge_colors.append('black')

        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, edge_color=edge_colors) 

        plt.show()

#Przykładowe użycie
if __name__ == '__main__':
    punkty = [
        (0, 0),
        (1, 1),
        (1, 0),
        (1, -1),
        (2, 1),
        (2, 0),
        (2, -1),
        (3, 1),
        (3, 0),
        (3, -1),
        (4, 0)
    ]

    adjList = {(0, 0): [((1,1), 7), ((1,0), 2), ((1,-1), 1)], 
               (1,1):[((2,1), 2), ((2,0), 4)],  (1,0):[((2,0),5), ((2,-1),6)], (1,-1):[((2,1),4), ((3,0),8)],
               (2,1):[((3,1),7), ((3,0), 1)], (2,0):[((3,1),3), ((2,-1),8), ((3,-1),3)], (2,-1):[((3,-1),3)],
               (3,1):[((4,0),1)], (3,0):[((4,0),3)], (3,-1):[((4,0),4)],
               (4,0):[]}
    n = len(punkty)
    start = (0, 0)
    end = (4, 0)

    solver = FordFulkerson(n, start, end, punkty)
    solver.config(start, end, adjList)
    print(solver.getMaxFlow())
    solver.getGraph()
    solver.draw()