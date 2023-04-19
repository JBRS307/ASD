#Macierz incydencji

#O(V+E)

def DFS(G, s):
    n = len(G)
    visited = [False]*n
    parent = [None]*n

    def DFSvisit(G, s, n):
        nonlocal visited, parent
        visited[s] = True
        print(s)
        for vert in G[s]:
            if not visited[vert]:
                parent[vert] = s
                DFSvisit(G, vert, n)
    
    DFSvisit(G, s, n)
    return visited, parent

if __name__ == "__main__":
    G = [
        [1, 2],
        [0, 2],
        [0, 1]
    ]
    v, p = DFS(G, 0)
    print(v)
    print(p)