from zad4testy import runtests

from collections import deque

def BFS(G, s, t):
    n = len(G)
    dist = [-1]*n
    parent = [[] for _ in range(n)]
    q = deque()
    q.append(s)
    dist[s] = 0

    while len(q) != 0:
        v = q.popleft()
        if(v == t):
            break
        for v_next in G[v]:
            if dist[v_next] == -1:
                q.append(v_next)
                dist[v_next] = dist[v]+1
                parent[v_next].append(v)
            elif dist[v_next] ==  dist[v]+1:
                parent[v_next].append(v)
    return dist[t], parent

def longer( G, s, t ):    
    path_len, sub_G = BFS(G, s, t) #sub_G to podgraf najkrótszych ścieżek od t do s, może być traktowany jak skierowany
    pass

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( longer, all_tests = True )

G = [
    [1, 2],
    [0, 2],
    [0, 1]
]
s = 0
t = 2

path_len, parent = BFS(G, s, t)

print(path_len)
print(*parent)