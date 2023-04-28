from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    parent = [None]*n
    visited = [False]*n
    dist = [float('inf')]*n
    q = PriorityQueue()
    dist[s] = 0

    q.put((0, s))
    while not q.empty():
        d, u = q.get()
        for v, value in G[u]:
            if not visited[v]:
                if d+value < dist[v]:
                    dist[v] = d+value
                    parent[v] = u
                    q.put((dist[v], v))
        visited[u] = True
    
    return parent, dist

if __name__ == "__main__":
    G = [
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

parent, dist = dijkstra(G, 0)
print(parent)
print()
print(dist)