from collections import deque

def BFS(G, s, t, parent):
    n = len(G)
    q = deque()
    visited = [False]*n
    q.append(s)
    visited[s] = True

    while len(q) != 0:
        u = q.popleft()
        for i in range(n):
            if G[u][i]:
                if not visited[i]:
                    q.append(i)
                    parent[i] = u
                    visited[i] = True
                    if i == t:
                        return True
    
    return False
        

def ford(G, s, t):
    n = len(G)
    parent = [None]*n
    max_flow = 0

    while BFS(G, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            path_flow = (G[parent[v]][v] if G[parent[v]][v] < path_flow else path_flow)
            v = parent[v]
        
        max_flow += path_flow

        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = u
        
    return max_flow

if __name__ == "__main__":
    G = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
    
    s = 0
    t = 5

    print(ford(G, s, t))
