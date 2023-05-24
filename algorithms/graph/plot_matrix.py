import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Macierz sąsiedztwa
A = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0]]

# Tworzenie grafu na podstawie macierzy sąsiedztwa
G = nx.from_numpy_array(np.array(A))

# Rysowanie grafu
nx.draw(G, with_labels=True)
plt.show()