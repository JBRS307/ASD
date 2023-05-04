#Negative dijkstra
#Graf musi byc skierowany

def neg_dijkstra(G, s):
    n = len(G)
    dist = [float('inf')]*n
    parent = [None]*n
    dist[s] = 0

    for _ in range(n-1):
        for u in range(n):
            for v, value in G[u]:
                if dist[u] != float('inf') and dist[v] > dist[u]+value:
                    dist[v] = dist[u]+value
                    parent[v] = u

    for u in range(n):
        for v, value in G[u]:
            if dist[u] != float('inf') and dist[v] > dist[u]+value:
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

    res = neg_dijkstra(G, 0)

    if res is not None:
        dist, parent = res
        print(*dist, end="\n\n")
        print(*parent)
