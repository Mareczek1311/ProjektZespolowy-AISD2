#input - graf (adjacency list)
#tworze liste W ktora bedzie posiadac wszystkie wierzcholki
#tworze pusta liste K ktora bedzie przechowywac wierzcholki z kamerami
#biore losowa krawedz a i b
#usuwam te wierzcholki z tej listy W
#usuwam wszystkie krawedzie ktore sa polaczone z a lub z b
#dodaje punkty a i b do listy K



"""
przykladowy graf wejsciowy:
"""

import random
import get_graph

#version 0.1


import networkx as nx
import matplotlib.pyplot as plt

#poki co algorytm naiwny
#biore losowa krawedz a i b

#w kolejnej wersji bede bral krawedz ktora ma najwiecej krawedzi

def znajdz_kamery(graf):
    wierzcholki = []
    kamery = []

    for key in graf:
        wierzcholki.append(key)

    while len(wierzcholki) > 0:
        print("W: ", wierzcholki, "  || K: ", kamery)
        a = random.choice(wierzcholki)
        b = None

        for node in graf[a]:
            if node in wierzcholki:
                b = node
                break
        
        if b == None:
            kamery.append(a)
            wierzcholki.remove(a)
            continue

        wierzcholki.remove(a)
        wierzcholki.remove(b)

        for key in graf[a]:
            if key in wierzcholki:
                wierzcholki.remove(key)
        
        for key in graf[b]:
            if key in wierzcholki:
                wierzcholki.remove(key)
        
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
    graf = get_graph.get_graph(graf)

    for key in graf:
        print(key, " -> ", graf[key])    

    kamery = znajdz_kamery(graf)
    print(kamery)
    draw(graf, kamery)