def print_arr(arr):
    for line in arr:
        for elem in line:
            print(elem, end="\t")
        print()


def multi_dijkstra(G):
    n = len(G)
    dist = [[elem for elem in line] for line in G]

    parent = [[u if G[u][v] != float('inf') else None for v in range(n)] for u in range(n)]

    for t in range(n):
        for u in range(n):
            for v in range(n):
                # dist[u][v] = min(dist[u][t]+dist[t][v], dist[u][v])
                if dist[u][t]+dist[t][v] < dist[u][v]:
                    dist[u][v] = dist[u][t]+dist[t][v]
                    parent[u][v] = u
    
    for i in range(n):
        parent[i][i] = None
    
    return dist, parent

if __name__ == "__main__":
    G = [
        [0,   5,  float('inf'), 10],
        [float('inf'),  0,  3,  float('inf')],
        [float('inf'), float('inf'), 0,   1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]

    dist, parent = multi_dijkstra(G)

    print_arr(dist)
    print()
    print_arr(parent)

    