#Algorytm znajdujący silnie spójne składowe
#Działa tylko dla skierowanych (dla nieskierowanych nie ma sensu)

#Graf silnie spójnych składowych musi być acykliczny, bo w przeciwnym razie sam jest jedną silnie spójną składową

from collections import deque

def strong(G):
    n = len(G)
    stack = deque() #Wierzchołki o najwyższym czasie przetworzenia zostaną dodane najpóżniej
    visited = [False]*n
    components = []

    def DFSvisit(s, curr_comp=None, T=False): #T - oznacza puszczanie DFS dla grafu transponowanego (z odwróconymi kierunkami)
        nonlocal G, stack, visited, n

        visited[s] = True

        if not T:
            for i in range(n):
                if G[s][i] and not visited[i]:
                    DFSvisit(i)
        else:
            for i in range(n):
                if G[i][s] and not visited[i]:
                    DFSvisit(i, curr_comp, T=True)
            curr_comp.append(s)
        
        if not T:
            stack.append(s)
    
    DFSvisit(0)
    visited = [False]*n
    while stack:
        curr_comp = []
        s = stack.pop()
        if not visited[s]:
            DFSvisit(s, curr_comp, T=True)
            components.append(curr_comp)
    
    return components


if __name__ == "__main__":
    G = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    ]

    print(*strong(G), sep='\n')


    

