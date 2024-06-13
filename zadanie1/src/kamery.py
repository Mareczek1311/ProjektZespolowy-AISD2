import random
from get_graph import get_graph
from random_graph import random_graph

import networkx as nx
import matplotlib.pyplot as plt

def znajdz_kamery_v2(graf):
    """!
    znajdz_kamery Metoda ktora znajduje kamery dla danego grafu
    @param graf - graf w postaci slownika gdzie kluczem jest wierzcholek a wartoscia lista sasiadow wierzcholka
    """
    wierzcholki = set(graf.keys())
    kamery = []

    while wierzcholki:
        # Znajdź wierzchołek o największym stopniu
        a = max(wierzcholki, key=lambda node: len(graf[node]))

        # Szukaj sąsiada wierzchołka a
        b = None
        for node in graf[a]:
            if node in wierzcholki:
                b = node
                break

        # Jeśli nie ma sąsiada wierzchołka a
        if b is None:
            kamery.append(a)
            wierzcholki.remove(a)
            continue

        # Usuń a, b i ich sąsiadów z wierzcholków
        wierzcholki.remove(a)
        wierzcholki.remove(b)
        for key in graf[a]:
            wierzcholki.discard(key)
        for key in graf[b]:
            wierzcholki.discard(key)

        # Dodaj kamery na a i b
        kamery.append(a)
        kamery.append(b)

    return kamery


def draw(graf, kamery):
    G = nx.DiGraph()

    G.add_nodes_from(graf.keys())

    for key in graf:
        for val in graf[key]:
            G.add_edge(key, val)

    colors = ['red' if node in kamery else 'blue' for node in G.nodes()]

    pos = {node: node for node in G.nodes()}

    nx.draw(G, pos, with_labels=True, node_size=400, node_color=colors, font_size=8, font_weight="bold")

    plt.grid(True)
    plt.show()

    

if __name__ == "__main__":
    graf = {(0, 0): [((-2, 2), 5), ((2, 2), 5), ((2, -2), 5), ((-2, -2), 5)], (-3, 3): [((10, 0), 6.0)], (3, 3): [((10, 0), 6.0)], (-2, 2): [((-3, 3), 5)], (2, 2): [((3, 3), 5)], (-2, -2): [((-3, -3), 5), ((-2, 2), 5)], (2, -2): [((3, -3), 5), ((-3, -3), 5), ((-2, -2), 5), ((3, 3), 5)], (-3, -3): [((10, 0), 6.0)], (3, -3): [((10, 0), 6.0)], (10, 0): []}
    graf = get_graph(graf)

    for key in graf:
        print(key, " -> ", graf[key])    

    kamery = znajdz_kamery_v2(graf)
    print(kamery)
    draw(graf, kamery)

    graf = random_graph(7, 'default')
    kamery = znajdz_kamery_v2(graf)
    draw(graf, kamery)   

    graf = random_graph(7, 'half_connections')
    kamery = znajdz_kamery_v2(graf)
    draw(graf, kamery)    
