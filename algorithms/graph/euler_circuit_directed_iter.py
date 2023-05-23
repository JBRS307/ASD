from collections import deque

def euler_circuit(G, s):
    n = len(G)
    edges = [len(G[i]) for i in range(n)]
    path = deque()
    circuit = []
    
    path.append(s)
    curr = s
    while path:
        if edges[curr]:
            path.append(curr)
            next_v = G[curr][edges[curr]-1]
            edges[curr] -= 1
            curr = next_v
        else:
            circuit.insert(0, curr)
            curr = path.pop()
    return circuit
