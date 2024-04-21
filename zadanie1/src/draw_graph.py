import networkx as nx
import matplotlib.pyplot as plt

def draw_tragarze(tragarze, kluby, siec):
    G = nx.Graph()
    
    for t in tragarze:
        if t.start_lub_end != None:
            G.add_node(t.id, pos=(t.start_lub_end, 2.5))
        elif t.rece_z_przodu:
            G.add_node(t.id, pos=(2, t.indexY))
        else:
            G.add_node(t.id, pos=(6, t.indexY))

    for t in siec:
        for tragarz in siec[t]:
            G.add_edge(t.id, tragarz.to.id, weight=tragarz.capacity)

    edge_labels = { (t1, t2): w['weight'] for t1, t2, w in G.edges(data=True)}


    pos = nx.get_node_attributes(G, 'pos')
    print(pos)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.axhline(y=0, color='k', linestyle='-', linewidth=1)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=1)

    plt.grid(True)
    plt.show()