from zad4testy import runtests

from collections import deque

def find_bridges(G, v):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    low = [-1]*n
    time_arr = [-1]*n
    time = 0
    def DFSvisit(s):
        nonlocal G, visited, parent, time, time_arr
        time += 1
        time_arr[s] = time
        low[s] = time
        visited[s] = True
        for child in G[s]:
            if not visited[child]:
                parent[child] = s
                DFSvisit(child)
                low[s] = low[child] if low[child] < low[s] else low[s]
            elif child != parent[s]:
                low[s] = time_arr[child] if time_arr[child] < low[s] else low[s]
        time += 1

    
    DFSvisit(v)
    for i in range(n):
        if low[i] == time_arr[i] and parent[i] is not None:
            return (i, parent[i])
    return None

def gen_sub_G(G, dist_s, dist_t, path):
    n = len(G)
    sub_G = [[] for _ in range(n)]
    for v in range(n):
        for next_v in G[v]:
            if dist_s[v] + dist_t[next_v] == path-1 or \
               dist_t[v] + dist_s[next_v] == path-1:
                sub_G[v].append(next_v)
    return sub_G
        

def BFS(G, s, t):
    n = len(G)
    dist = [-1]*n
    q = deque()
    q.append(s)
    dist[s] = 0

    while len(q) != 0:
        v = q.popleft()
        for v_next in G[v]:
            if dist[v_next] == -1:
                q.append(v_next)
                dist[v_next] = dist[v]+1
    return dist

def longer( G, s, t ):
    dist_s = BFS(G, s, t)
    dist_t = BFS(G, t, s)
    path = dist_s[t]
    sub_G = gen_sub_G(G, dist_s, dist_t, path)
    return find_bridges(sub_G, s)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )

# G = [
#     [1],
#     [0],
#     []
# ]

# G = [
#     [1, 6],
#     [0, 2],
#     [1, 3, 6],
#     [2, 4, 5],
#     [3, 5],
#     [3, 4],
#     [0, 2, 7],
#     [6]
# ]

# s = 0
# t = 2

# parent = BFS(G, s, t)
# print(*parent)
# undirect(parent)
# print(*parent)

# print(longer(G, s, t))