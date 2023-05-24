from copy import deepcopy
#Na kolosie graf trzeba skopiować ręcznie

def DFS(G, s):
    n = len(G)
    visited_edges = [0]*n
    # parent = [None]*n
    euler_circuit = []
    
    def DFSvisit(G, s):
        nonlocal visited_edges, euler_circuit
        while visited_edges[s] < n:
                if G[s][visited_edges[s]]:
                    G[visited_edges[s]][s] = 0
                    visited_edges[s] += 1
                    DFSvisit(G, visited_edges[s]-1)
                else: 
                    visited_edges[s] += 1
        euler_circuit.append(s)
    
    DFSvisit(G, s)
    return euler_circuit

if __name__ == "__main__":
    G = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

    graph = deepcopy(G)
    circuit = DFS(graph, 0)
    print(circuit)
