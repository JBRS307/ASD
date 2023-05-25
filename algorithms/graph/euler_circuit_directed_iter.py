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
            circuit.append(curr)
            curr = path.pop()
    return circuit[::-1]

if __name__ == "__main__":
    G = [
        [1, 2],
        [0, 2],
        [0, 1]
    ]

    circuit = euler_circuit(G, 0)
    print(circuit)

