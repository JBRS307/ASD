#Zastosowania DFS
#1. Spójność
#2. Dwudzielność
#3. Wykrywanie cykli
#4. Sortowanie topologiczne
#5. Silnie spójne składowe
#6. Wyznaczanie cyklu Eulera
#7. Mosty/punkty artykulacji

#Macierz adiacencji

#O(V^2)

def DFS(G, s):
    n = len(G)
    visited = [False]*n
    parent = [None]*n

    def DFSvisit(G, s, n):
        nonlocal visited, parent
        visited[s] = True
        print(s)
        for i in range(n):
            if G[s][i]:
                if not visited[i]:
                    parent[i] = s
                    DFSvisit(G, i, n)
    
    DFSvisit(G, s, n)
    return visited, parent

if __name__ == "__main__":
    G = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    v, p = DFS(G, 0)
    print(v)
    print(p)
    