import networkx as nx
import matplotlib.pyplot as plt

graph = [
    [(1, 3), (2, 4)],
    [(0, 3), (2, 1), (3, 2)],
    [(0, 4), (1, 1), (3, 5)],
    [(1, 2), (2, 5), (4, 6)],
    [(3, 6), (5, 7)],
    [(4, 7), (6, 8)],
    [(5, 8), (7, 9)],
    [(6, 9), (8, 10)],
    [(7, 10), (9, 11)],
    [(8, 11)]
]

G = nx.Graph()
for i in range(len(graph)):
    for j in range(len(graph[i])):
        G.add_edge(i, graph[i][j][0], weight=graph[i][j][1])

pos = nx.spring_layout(G)
nx.draw(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw_networkx_labels(G,pos)

plt.show()