def list_to_matrix(G):
    n = len(G)
    G_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for neighbor in G[i]:
            G_matrix[i][neighbor[0]] = neighbor[1]
    
    return G_matrix


def neg_dijkstra(G, s):
    n = len(G)
    parent = [None]*n
    dist = [float('inf')]*n
    dist[s] = 0

    for _ in range(n-1):
        for u in range(n):
            for v in range(n):
                if G[u][v] != float('inf'):
                    if dist[u] != float('inf') and dist[v] > dist[u]+G[u][v]:
                        dist[v] = dist[u]+G[u][v]
                        parent[v] = u
    
    for u in range(n):
        for v in range(n):
            if G[u][v] != float('inf'):
                if dist[u] != float('inf') and dist[v] > dist[u]+G[u][v]:
                    print("Infinite negative cycle")
                    return
    
    return dist, parent

if __name__ == "__main__":
    G = [
        [(1, 5), (2, 3)],
        [(2, 2), (3, 6)],
        [(3, 7), (4, 4), (5, 2)],
        [(4, -1), (5, 1)],
        [(5, -2)],
        [(6, 3)],
        [(7, -1), (8, -2)],
        [(9, -3)],
        [(9, -4)],
        []
    ]

    G = list_to_matrix(G)

    res = neg_dijkstra(G, 0)

    if res is not None:
        dist, parent = res
        print(*dist, end="\n\n")
        print(*parent)