from zad1testy import runtests

def get_buildings(dp, buildings, students, parent, cost, idx, p):
    if idx is None:
        return buildings
    if idx == 0:
        if p > cost[0]:
            buildings.append(0)
        return buildings
    if dp[idx-1][p] == dp[idx][p]:
        return get_buildings(dp, buildings, students, parent, cost, idx-1, p)
    buildings.append(idx)
    return get_buildings(dp, buildings, students, parent, cost, parent[idx], p-cost[idx])

def select_buildings(T, p):
    n = len(T)
    for i in range(n):
        T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    T.sort(key=lambda x: x[2])
    cost = [0]*n
    parent = [None]*n
    students = [0]*n

    for i in range(n):
        cost [i] = T[i][3]
        students[i] = (T[i][2]-T[i][1])*T[i][0]
        for j in range(i-1, -1, -1):
            if T[j][2] < T[i][1]:
                parent[i] = j
                break
    
    dp = [[0]*(p+1) for _ in range(n)]

    for j in range(p+1):
        if cost[0] <= j:
            dp[0][j] = students[0]

    for i in range(1, n):
        for j in range(p+1):
            dp[i][j] = dp[i-1][j]
            if parent[i] is not None and cost[i] < j:
                dp[i][j] = max(dp[i][j], dp[parent[i]][j-cost[i]]+students[i])
            elif parent[i] is None and cost[i] < j:
                dp[i][j] = max(dp[i][j], students[i])
    
    buildings = []
    get_buildings(dp, buildings, students, parent, cost, n-1, p)
    for i in range(len(buildings)):
        buildings[i] = T[buildings[i]][4]
    return sorted(buildings)

runtests( select_buildings ) 
