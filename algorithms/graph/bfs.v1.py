from collections import deque

#Zastosowania
#1. Najkrótsze ścieżki (w sensie liczby krawędzi)
#2. Testowanie spójności
#3. Testowanie dwudzielności
#4. Wykrywanie cykli

#Macierz adiacencji

#O(V^2)

def BFS(G, v):
    n = len(G)
    q = deque()
    visited = [False]*n
    parent = [None]*n
    q.append(v)

    visited[v] = True
    while len(q) != 0:
        s = q.popleft()
        # if visited[s]: continue
        print(s, end=' ')
        # visited[s] = True
        for i in range(n):
            if G[s][i]:
                if not visited[i]:
                    q.append(i)
                    parent[i] = s
                    visited[i] = True
    print()
    return visited, parent

if __name__ == "__main__":
    G = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

    v, p = BFS(G, 0)
    print(v)
    print(p)



