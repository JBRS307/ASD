from copy import deepcopy
#Na kolosie graf trzeba skopiować ręcznie

def DFS(G, s):
    n = len(G)
    visited_edges = [0]*n
    # parent = [None]*n
    euler_circuit = []
    
    def DFSvisit(G, s):
        nonlocal visited_edges, euler_circuit
        for i in range(visited_edges[s], len(G[s])):
                if G[s][i]:
                    G[i][s] = 0
                    visited_edges[s] = i+1
                    DFSvisit(G, i)
        euler_circuit.insert(0, s)
    
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
