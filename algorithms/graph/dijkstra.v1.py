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
            return dist, parent
        
        for i in range(n):
            if min_ind != i and dist[min_ind] + G[min_ind][i] < dist[i]:
                dist[i] = dist[min_ind] + G[min_ind][i]
                parent[i] = min_ind
        
        visited[min_ind] = True
