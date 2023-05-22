#Wszystkie funkcje są dla grafu nieskierowanego ważonego

def edges_to_list(G, n):
    G_list = [[] for _ in range(n)]

    for edge in G:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    
    return G_list

def edges_to_matrix(G, n):
    G_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    for edge in G:
        G[edge[0]][edge[1]] = edge[2]
        G[edge[1]][edge[0]] = edge[2]
    
    return G_matrix

def matrix_to_list(G):
    n = len(G)
    G_list = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                G_list[i].append((j, G[i][j]))
    
    return G_list

def matrix_to_list_unweighted(G):
    n = len(G)
    G_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                G_list[i].append(j)
    
    return G_list

def matrix_to_edges(G):
    n = len(G)
    G_edges = []
    
    for i in range(n):
        for j in range(i+1, n):
            if i != j:
                G_edges.append((i, j, G[i][j]))
    
    return G_edges

def list_to_matrix(G):
    n = len(G)
    G_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for neighbor in G[i]:
            G_matrix[i][neighbor[0]] = neighbor[1]
    
    return G_matrix

def list_to_edges(G): #Później
    n = len(G)
    G_edges = []

    for i in range(n):
        for v in G[i]:
            a = i
            b = v[0]
            if a > b:
                a, b = b, a
            
            if (a, b, v[1]) not in G_edges:
                G_edges.append((a, b, v[1]))
    
    return G_edges


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

    print(*matrix_to_list_unweighted(G), sep=",\n")



