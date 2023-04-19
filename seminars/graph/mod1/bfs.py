#BFS korzystający z macierzy adiacencji

from collections import deque

def BFS(G):
    V = len(G)
    visited = [False]*V
    q = deque()

    q.append(0)
    while len(q) != 0:
        s = q[0]
        q.popleft()
        visited[s] = True
        for i in range(V):
            if G[s][i]:
                if not visited[i]:
                    q.append(i)