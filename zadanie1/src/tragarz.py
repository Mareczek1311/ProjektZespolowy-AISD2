
from random_tragarze import random_tragarze
from fordfulkerson import FordFulkerson


def main():
    tragarze = random_tragarze(16, '50/50')
    solver = FordFulkerson(len(tragarze), tragarze["start"], tragarze["end"], tragarze["punkty"])
    solver.config(tragarze["start"], tragarze["end"], tragarze["adjList"])
    print(solver.getMaxFlow())
    print("Graph:")
    solver.getGraph()
    solver.drawTragarze()

if __name__ == "__main__":
    main()