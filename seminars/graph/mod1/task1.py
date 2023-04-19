#Policz ile graf ma spójnych składowych

def DFS(G):
    V = len(G)
    visited = [False]*V

    def visitDFS(G, s):
        nonlocal visited
        visited[s] = True
        for i in G[s]:
            if not visited[i]:
                visited[i] = True
                visitDFS(G, i)

    res = 0
    for i in range(V):
        if not visited[i]:
            res += 1
            visitDFS(G, i)
    
    return res