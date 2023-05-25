#1. Wykonujemy DFS, usuwając krawędzie, po których przeszliśmy (zapamiętujemy, że już ich nie używamy)
#2. Do danego wierzchołka możemy wejść dowolną liczbę razy (usuwamy visited)
#3. Po przetworzeniu wierzchołka dopisujemy go na początek cyklu (dany wierzchołek można przetworzyć kilka razy)
#4. Praca kończy się, gdy nie mamy dokąd już iść

#Zdecydowanie łatwiej dla grafu skierowanego

def DFS(G, s):
    n = len(G)
    visited_edges = [0]*n
    # parent = [None]*n
    euler_circuit = []
    
    def DFSvisit(G, s):
        nonlocal visited_edges, euler_circuit
        while visited_edges[s] < len(G[s]):
                visited_edges[s] += 1
                DFSvisit(G, G[s][visited_edges[s]-1])
        euler_circuit.append(s)
    
    DFSvisit(G, s)
    return euler_circuit[::-1]

if __name__ == "__main__":
    G = [
        [1, 2],
        [0, 2],
        [0, 1]
    ]

    circuit = DFS(G, 0)
    print(circuit)
