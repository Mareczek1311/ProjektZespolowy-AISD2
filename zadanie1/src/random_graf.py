import networkx as nx
import matplotlib.pyplot as plt

# Parametry grafu: liczba wierzchołków i liczba krawędzi
n = 10
m = 15

# Generowanie losowego grafu z ustaloną liczbą krawędzi
G = nx.gnm_random_graph(n, m)
pos = nx.spring_layout(G)


# Rysowanie grafu
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=8, font_weight="bold")
plt.show()



for node, pos in pos.items():
    print(f"Node: {node}, position: {pos}")
    