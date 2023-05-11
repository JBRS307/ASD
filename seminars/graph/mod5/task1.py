#Sieć fabryk + sieć sklepów, która odbiera to co fabryki wyprodukują + sieć kolejowa
#Sklepy i fabryki mają ograniczoną przepustowość
#Obliczyć ile maksymalnie można sprzedać

from copy import deepcopy

INT_MAX = (1<<31)-1
# print(INT_MAX)

def modify_problem(graph, S, T):
    G = deepcopy(graph)
    n = len(graph)
    
    G.apend([0 for _ in range(n)])
    G.apend([0 for _ in range(n)])

    for i in range(n+2):
        G[i].extend([0, 0])
    
    for v, w in S:
        G[n][v] = w
    
    for v, w in T:
        G[v][n+1] = w
    
    return ford_fulkerson(G, n, n+1)
    


