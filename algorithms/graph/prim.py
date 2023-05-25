#tree dijkstra

from queue import PriorityQueue


def edge_to_list(G, n):
    new_G = [[] for _ in range(n)]
    for edge in G:
        new_G[edge[0]].append((edge[1], edge[2]))
        new_G[edge[1]].append((edge[0], edge[2]))
    
    return new_G

def tree_dijkstra(G, s):
    n = len(G)
    parent = [None]*n
    visited = [False]*n
    dist = [float('inf')]*n
    dist[s] = 0
    q = PriorityQueue()

    q.put((0, s))
    while not q.empty():
        _, u = q.get()
        for v, value in G[u]:
            if not visited[v] and value < dist[v]:
                dist[v] = value
                parent[v] = u
                q.put((dist[v], v))
        visited[u] = True
    
    return parent

if __name__ == "__main__":
#     G = [
#     [(1, 3), (2, 4)],
#     [(0, 3), (2, 1), (3, 2)],
#     [(0, 4), (1, 1), (3, 5)],
#     [(1, 2), (2, 5), (4, 6)],
#     [(3, 6), (5, 7)],
#     [(4, 7), (6, 8)],
#     [(5, 8), (7, 9)],
#     [(6, 9), (8, 10)],
#     [(7, 10), (9, 11)],
#     [(8, 11)]
# ]

#     print(*tree_dijkstra(G, 0))

    # G = [
    #     (0, 1, 2),
    #     (1, 2, 3),
    #     (2, 3, 1),
    #     (0, 3, 4),
    #     (3, 4, 5),
    #     (4, 5, 6),
    #     (5, 6, 7),
    #     (6, 7, 8),
    #     (7, 8, 9),
    #     (8, 9, 10),
    #     (9, 0, 11),
    #     (0, 2, 12),
    #     (2, 4, 13),
    #     (4, 6, 14),
    #     (6, 8, 15)
    # ]

    # G = edge_to_list(G, len(G))

    # print(*tree_dijkstra(G, 0))

    # G = [
    #     [(1, 1), (8, 2)],
    #     [(0, 1), (2, 3), (4, 3)],
    #     [(1, 3), (3, 5)],
    #     [(2, 5), (4, 2), (6, 1)],
    #     [(1, 3), (3, 2), (5, 3), (8, 1)],
    #     [(4, 3), (6, 8), (7, 1)],
    #     [(3, 1), (5, 8), (7, 4)],
    #     [(5, 1), (6, 4), (8, 7)],
    #     [(0, 2), (4, 1), (7, 7)]
    # ]
    
    # print(*tree_dijkstra(G, 0))

    G = [
    [(1,2),(3,4)],#0
    [(0,2),(2,5)],#1
    [(1,5),(3,1),(4,7)],#2
    [(2,1),(4,9), (0,4)],#3
    [(2,7),(3,9)],#4
    ]

    print(tree_dijkstra(G, 0))