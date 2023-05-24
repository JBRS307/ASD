# Wszystko działa jak zwykły dijkstra dla reprezentacji macierzowej, tylko w tablicy dist, oprócz odległości
# zapisujemy też to ile benzyny zostało nam w danym polu. Jeśli w polu jest stacja benzynowa to ilość pozostałej
# benzyny jest równa d.


def jak_dojade(G, P, d, a, b):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    dist = [(float('inf'), -1) for _ in range(n)]
    dist[a] = (0, d)

    while True:
        min_dist = float('inf')
        min_ind = None
        for i in range(n):
            if not visited[i] and dist[i][0] < min_dist:
                min_dist = dist[i][0]
                min_ind = i

        if min_ind is None:
            break
        
        for i in range(n):
            if min_ind != i and G[min_ind][i] != -1 and dist[min_ind][0] + G[min_ind][i] < dist[i][0] and \
               dist[min_ind][1]-G[min_ind][i] >= 0:
                if i in P:
                    dist[i] = (dist[min_ind][0] + G[min_ind][i], d)
                else:
                    dist[i] = (dist[min_ind][0] + G[min_ind][i], dist[min_ind][1]-G[min_ind][i])
                parent[i] = min_ind
        
        visited[min_ind] = True
        curr = min_ind


    if dist[b][0] == float('inf'):
        return None
    
    path = []

    curr = b
    while curr != parent[a]:
        path.append(curr)
        curr = parent[curr]
    
    return path[::-1]


if __name__ == "__main__":
    G = [[-1, 6,-1, 5, 2],
         [-1,-1, 1, 2,-1],
         [-1,-1,-1,-1,-1],
         [-1,-1, 4,-1,-1],
         [-1,-1, 8,-1,-1]]
    
    P = [0,1,3]

    print(jak_dojade(G, P, 5, 0, 2))
    print(jak_dojade(G, P, 3, 0, 2))
