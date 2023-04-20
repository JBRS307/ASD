#Sprawdź czy w skierowanym grafie spójnym acyklicznym jest ścieżka Hamiltona

def hamilton(G):
    n = len(G)
    visited = [False]*n
    dag = []

    def DFS(G, s):
        nonlocal dag, visited

        for v in G[s]:
            if not visited[v]:
                DFS(G, v)
        dag.append(s)
    
    DFS(G, 0)
    for i in range(1, n):
        if not dag[i-1] in G[i]:
            return False
    return True

