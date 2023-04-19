#DFS z wykorzystaniem macierzy incydencji

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
    
    visitDFS(G, 0)