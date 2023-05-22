def find_bridges(G):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    low = [0]*n
    bridges = []
    time_arr = [-1]*n
    time = 0

    def DFSvisit(s):
        nonlocal G, visited, parent, time_arr, time, low
        visited[s] = True
        time += 1
        time_arr[s] = time
        low[s] = time
        for child in G[s]:
            if not visited[child]:
                parent[child] = s
                DFSvisit(child)
                low[s] = low[child] if low[child] < low[s] else low[s] #min(low[child], low[s])
            elif child != parent[s]:
                low[s] = time_arr[child] if time_arr[child] < low[s] else low[s] #min(time[child], low[s])
        time += 1

    DFSvisit(0)
    for i in range(n):
        if low[i] == time_arr[i] and parent[i] is not None:
            bridges.append((i, parent[i]))
    
    return bridges

if __name__ == "__main__":
    G = [
        [1, 6],
        [0, 2],
        [1, 3, 6],
        [2, 4, 5],
        [3, 5],
        [3, 4],
        [0, 2, 7],
        [6]
    ]

    print(find_bridges(G))

    G = [
        [1, 2, 3],
        [0, 2],
        [0, 1],
        [0, 4],
        [3]
    ]

    print(find_bridges(G))

    G = [
        [1, 2],
        [0, 2, 3, 4, 6],
        [0, 1],
        [1, 5],
        [1, 5],
        [3, 4],
        [1]
    ]

    print(find_bridges(G))
