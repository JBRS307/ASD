def list_to_matrix(G):
    n = len(G)
    M = [[0]*n for _ in range(n)]

    for s in range(n):
        for t in G[s]:
            M[s][t[0]] = t[1]
    
    return M

def dijkstra(G, s):
    n = len(G)
    parent = [None]*n
    visited = [False]*n
    dist = [float('inf')]*n
    dist[s] = 0

    while True:
        min_dist = float('inf')
        min_ind = None
        for i in range(n):
            if dist[i] < min_dist and not visited[i]:
                min_dist = dist[i]
                min_ind = i

        if min_ind is None:
            return parent
        
        for i in range(n):
            if not visited[i] and min_ind != i and G[min_ind][i] and G[min_ind][i] < dist[i]:
                dist[i] = G[min_ind][i]
                parent[i] = min_ind
        
        visited[min_ind] = True

if __name__ == "__main__":
    G = [
    [(1,2),(3,4)],#0
    [(0,2),(2,5)],#1
    [(1,5),(3,1),(4,7)],#2
    [(2,1),(4,9), (0,4)],#3
    [(2,7),(3,9)],#4
    ]

    G = list_to_matrix(G)

    print(dijkstra(G, 0))



