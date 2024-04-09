import networkx as nx
import matplotlib.pyplot as plt

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
]

def findMin(punkty):
    min = punkty[0]

    #find min
    for i in range(1, len(punkty)):
        if punkty[i][1] < min[1]:
            min = punkty[i]
        elif punkty[i][1] == min[1]:
            if punkty[i][0] < min[0]:
                min = punkty[i]
    return min


#wyznacznik
def det(p1, p2, p3):
    return p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1]

def graham(punkty):
    min = findMin(punkty)
    print(min)

    #bubble sort (n^2) zla zlozonosc
    for i in range(1, len(punkty)):
        for j in range(i+1, len(punkty)):
            wyz = det(min, punkty[i], punkty[j])
            if wyz < 0:
                punkty[i], punkty[j] = punkty[j], punkty[i]
            if wyz == 0:
                if punkty[i][0] < punkty[j][0]:
                    punkty[i], punkty[j] = punkty[j], punkty[i]
    print(punkty)

    stack = []
    stack.append(min)
    stack.append(punkty[1])
    stack.append(punkty[2])

    #grahamka ;)
    for i in range(3, len(punkty)):
        while det(stack[-2], stack[-1], punkty[i]) < 0:
            stack.pop()
        stack.append(punkty[i])
    stack.append(min)
    print(stack)
    return stack

res = graham(punkty)

G = nx.DiGraph()

G.add_nodes_from([point for point in punkty])

G.add_edges_from([(res[i], res[i+1]) for i in range(len(res)-1)])

pos = {node: node for node in G.nodes()}

nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")

plt.axhline(y=0, color='k', linestyle='-', linewidth=1)
plt.axvline(x=0, color='k', linestyle='-', linewidth=1)

plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Graf w układzie współrzędnych OX i OY')
plt.grid(True)
plt.show()
