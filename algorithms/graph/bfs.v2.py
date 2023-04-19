from collections import deque

#Macierz incydencji

#O(V+E)

def BFS(G, v):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    q = deque()

    q.append(v)
    visited[v] = True
    while len(q) != 0:
        s = q.popleft()
        # if visited[s]: continue
        print(s, end=' ')
        # visited[s] = True
        for vert in G[s]:
            if not visited[vert]:
                q.append(vert)
                parent[vert] = s
                visited[vert] = True
    print()
    return visited, parent

if __name__ == "__main__":
    G = [
        [1, 2],
        [0, 2],
        [0, 1]
    ]
    v, p = BFS(G, 0)
    print(v)
    print(p)