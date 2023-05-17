import networkx as nx
import matplotlib.pyplot as plt

# Lista krawędzi
edges = [
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 1),
    (0, 3, 4),
    (3, 4, 5),
    (4, 5, 6),
    (5, 6, 7),
    (6, 7, 8),
    (7, 8, 9),
    (8, 9, 10),
    (9, 0, 11),
    (0, 2, 12),
    (2, 4, 13),
    (4, 6, 14),
    (6, 8, 15)
]

edges_2 = [
    (2, 3, 1),
    (0, 1, 2),
    (1, 2, 3),
    (3, 4, 5),
    (4, 5, 6),
    (5, 6, 7),
    (6, 7, 8),
    (7, 8, 9),
    (8, 9, 10)
]

# Tworzenie grafu
G = nx.Graph()
G.add_weighted_edges_from(edges_2)

# Rysowanie grafu
pos = nx.spring_layout(G)
nx.draw(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# Wyświetlenie grafu
plt.show()