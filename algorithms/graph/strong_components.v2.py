from collections import deque

def transpone_graph(G, n):
    Gt = [[] for _ in range(n)]

    for s in range(n):
        for t in G[s]:
            Gt[t].append(s)

    return Gt

def strong(G):
    n = len(G)
    visited = [False]*n
    stack = deque()
    components = []

    def DFSvisit(G, s, current_comp=None, T=False):
        nonlocal visited, stack, n

        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                if not T:
                    DFSvisit(G, u)
                else:
                    DFSvisit(G, u, current_comp, T=True)

        if not T:
            stack.append(s)
        else:
            current_comp.append(s)
    

    DFSvisit(G, 0)
    visited = [False]*n
    Gt = transpone_graph(G, n)
    while stack:
        s = stack.pop()
        current_comp = []
        if not visited[s]:
            DFSvisit(Gt, s, current_comp, T=True)
            components.append(current_comp)
    
    return components


if __name__ == "__main__":
    G = [
        [1],
        [2],
        [0, 3, 8],
        [4, 6],
        [5],
        [3],
        [5],
        [8],
        [9],
        [5, 10],
        [3, 7]
    ]

    print(*strong(G), sep="\n")