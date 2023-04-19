#Sprawdź czy graf jest dwudzielnym za pomocą BFS

from collections import deque

def is_bipartite(G):
    V = len(G)
    color = [0]*V
    q = deque()

    q.append(0)
    color[0] = 1
    while len(q) != 0:
        s = q[0]
        q.popleft()
        for i in range(V):
            if G[s][i]:
                if color[i] == 0:
                    color[i] = 3-color[s]
                elif color[i] == color[s]:
                    return False
                q.append(i)
    
    return True
