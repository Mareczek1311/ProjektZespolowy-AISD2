import networkx as nx
import matplotlib.pyplot as plt

def draw_tragarze(tragarze, kluby):
    G = nx.Graph()
    print()
    
    tragarze_z_rekoma_z_przodu = []
    tragarze_z_rekoma_z_tylu = []
    
    for t in tragarze:
        print(t)
        if t.rece_z_przodu:
            G.add_node(t.id, pos=(1, t.indexY))
            tragarze_z_rekoma_z_przodu.append(t)
        else:
            G.add_node(t.id, pos=(5, t.indexY))
            tragarze_z_rekoma_z_tylu.append(t)

    for t1 in tragarze_z_rekoma_z_przodu:
        for t2 in tragarze_z_rekoma_z_tylu:
            if t1.id_ulubionego_klubu == t2.id_ulubionego_klubu or kluby[t1.id_ulubionego_klubu].sprawdzRelacje(t2.id_ulubionego_klubu):
                G.add_edge(t1.id, t2.id)
    
    pos = nx.get_node_attributes(G, 'pos')
    print(pos)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold")

    plt.axhline(y=0, color='k', linestyle='-', linewidth=1)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=1)

    plt.grid(True)
    plt.show()