
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

    

class NetworkSolver:
    def __init__(self, n, s, t):
        self.inf = float("inf")
        self.n = n
        self.s = s
        self.t = t
        self.graph = {}
        self.visited = []
        self.visitedToken = 1
        self.maxFlow = 0
        self.solved = False

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
                print("  ->", edge.to, edge.capacity, edge.flow)     

    def getMaxFlow(self):
        self.execute()
        return self.maxFlow
    
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

punkty = [
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
    (7, 7)
]

n = len(punkty) # num of nodes
s = punkty[1]
t = punkty[-1]
solver = NetworkSolver(n, s, t)

solver.addEdge(s, punkty[0], 1)

solver.addEdge(punkty[0], t, 1)

print(solver.getMaxFlow())

#get graph from solver

solver.getGraph()
