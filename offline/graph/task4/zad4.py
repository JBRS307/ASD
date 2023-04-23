#Jakub Rękas

#Algorytm generuje podgraf najkrótszych ścieżek z s do t (tudzież z t do s, w nieskierowanym to bez znaczenia).
#Następnie w tym podgrafie wyszukiwane są mosty, jeśli istnieje CHOĆBY JEDEN to znaczy, że da się usunąć jedną krawędź
#z głównego grafu tak, aby najkrótsza ścieżka została wydłużona.
#
#1. Na początku odpalamy dwa razy algorytm BFS, raz z wierzchołka s, drugi raz z wierzchołka t.
#Pierwsze wywołanie zwraca tablicę odległości od wierzchołka s (dist_s[]), druga od wierzchołka t (dist_t[]). (tablice domyślnie
#inicjalizowane -1). Jeśli po pierwszym wywołaniu BFS odległość od s do t wynosi -1, to znaczy, że wierzchołki nie leżą na tej samej
#spójnej składowej i należy zwrócić None.
#2. (jeśli funkcja longer nie zwróciła do tego momentu None) 
#Generujemy podgraf najkrótszych ścieżek od s do t korzystając z obu tablic dist_s[],
#dist_t[] i długości najkrótszej ścieżki. Sąsiednie wierzchołki v oraz u leżą na najkrótszej ścieżce jeśli ich suma
#odległości od s i t (lub t i s) jest równa (długości najkrótszej ścieżki)-1. Przechodzimy w ten sposób przez cały graf G.
#Na każdą parę wierzchołków natrafimy 2 razy i oba wierzchołki zostaną dodane do swoich list w reprezentacji listowej podgrafu
#najkrótszych ścieżek. Funkcja zwraca reprezentację listową nieskierowanego podgrafu najkrótszych ścieżek od s do t.
#3. Na koniec w podgrafie najkrótszych ścieżek wyszukujemy mosty (standardowym algorytmem do wyszukiwania mostów
#bazującym na DFS). Jeśli jakiś most zostanie znaleziony, zwracamy go, jeśli nie, to zwracamy None.
#
#Złożoność obliczeniowa O(V+E)
#Złożoność pamięciowa O(V+E)

from zad4testy import runtests

from collections import deque

def find_bridges(G, v): #O(V+E)
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    low = [-1]*n
    time_arr = [-1]*n
    time = 0
    def DFSvisit(s):
        nonlocal G, visited, parent, time, time_arr
        time += 1
        time_arr[s] = time
        low[s] = time
        visited[s] = True
        for child in G[s]:
            if not visited[child]:
                parent[child] = s
                DFSvisit(child)
                low[s] = low[child] if low[child] < low[s] else low[s]
            elif child != parent[s]:
                low[s] = time_arr[child] if time_arr[child] < low[s] else low[s]
        time += 1

    
    DFSvisit(v)
    for i in range(n):
        if low[i] == time_arr[i] and parent[i] is not None:
            return (i, parent[i])
    return None

def gen_sub_G(G, dist_s, dist_t, path): #O(V+E)
    n = len(G)
    sub_G = [[] for _ in range(n)]
    for v in range(n):
        for next_v in G[v]:
            if dist_s[v] + dist_t[next_v] == path-1 or \
               dist_t[v] + dist_s[next_v] == path-1:
                sub_G[v].append(next_v)
    return sub_G
        

def BFS(G, s, t): #O(V+E)
    n = len(G)
    dist = [-1]*n
    q = deque()
    q.append(s)
    dist[s] = 0

    while len(q) != 0:
        v = q.popleft()
        for v_next in G[v]:
            if dist[v_next] == -1:
                q.append(v_next)
                dist[v_next] = dist[v]+1
    return dist

def longer( G, s, t ):
    dist_s = BFS(G, s, t)
    path = dist_s[t]
    if path == -1:
        return None
    dist_t = BFS(G, t, s)
    sub_G = gen_sub_G(G, dist_s, dist_t, path)
    return find_bridges(sub_G, s)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )