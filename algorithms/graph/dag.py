#sortowanie topologiczne (działa dla grafów skierowanych)
#1. Uruchamiamy DFS
#2. Po przetworzeniu wierzchołka dopisujemy go na początku listy

#Macierz incydencji

def DFS(G, s):
    n = len(G)
    # parent = [None]*n
    visited = [False]*n

    graph_sorted = []

    def DFSvisit(G, s):
        nonlocal graph_sorted, visited
        # nonlocal parent
        visited[s] = True
        for vert in G[s]:
            if not visited[vert]:
                # parent[vert] = s
                DFSvisit(G, vert)
        graph_sorted.insert(0, [s, G[s]])
    
    DFSvisit(G, s)
    return graph_sorted

if __name__ == "__main__":
    G = [
        [2],
        [2],
        [1]
    ]

    graph_sorted = DFS(G, 0)
    print(*graph_sorted)
