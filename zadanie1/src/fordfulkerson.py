import networkx as nx
import matplotlib.pyplot as plt

class Edge:
    def __init__(self, fr, to, capacity):
        self.fr = fr
        self.to = to
        self.capacity = capacity #constant
        self.flow = 0
    
    def isResidual(self):
        return self.capacity == 0
    
    def remainingCapacity(self):
        return self.capacity - self.flow

    def augment(self, flow):
        self.flow += flow
        self.reverse.flow -= flow

    

class FordFulkerson:
    def __init__(self, n, s, t, punkty):
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
        self.execute()
        for node in self.graph:
            print(node)
            for edge in self.graph[node]:
                print("  ->", edge.to, " Capacity: ", edge.capacity, " Flow: ", edge.flow) 

        return self.graph    

    def getMaxFlow(self):
        self.execute()
        return "Max flow: " +  str(self.maxFlow)
    
    def execute(self):
        if self.solved:
            return
        self.solved = True
        self.solve()
    
    def solve(self):
        #f is 1 becouse we need to enter the loop
        f = 1
        
        while(f != 0):
            f = self.dfs(self.s, float("inf"))
            self.visited = []
            self.maxFlow += f

    def dfs(self, node, flow):
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
        self.s = s
        self.t = t

        for node in adjList:
            for edge in adjList[node]:
                self.addEdge(node, edge[0], edge[1])

    def draw(self):
        G = nx.DiGraph()

        G.add_nodes_from([node for node in self.punkty])
        for node in self.graph:
            for edge in self.graph[node]:
                G.add_edge(node, edge.to, capacity=edge.capacity, flow=edge.flow)

        pos = {node: node for node in G.nodes()}
        edge_labels = {}
        edge_labels_residual = {}
        
        for node in G.nodes():
            for edge in G.edges(node, data=True):
                if edge[2]['capacity'] != 0:
                    edge_labels[(edge[0], edge[1])] = str(edge[2]['flow']) + "/" + str(edge[2]['capacity'])
                else:
                    edge_labels_residual[(edge[0], edge[1])] = edge[2]['flow']

        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')

        nx.draw_networkx_edge_labels(G, pos, bbox=None, edge_labels=edge_labels_residual, verticalalignment="top",  horizontalalignment ="right", font_size=6, font_color='red')

        nx.draw_networkx_edge_labels(G, pos, bbox=None, edge_labels=edge_labels, verticalalignment="bottom",   horizontalalignment ="left", font_size=6)
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