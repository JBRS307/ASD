from kol2atesty import runtests
from math import inf

def get_switches(dp, n):
    if dp[n-1][1][0] < dp[n-1][0][0]:
        driver = 1
    else:
        driver = 0
    
    switches = []
    i = n-1
    while dp[i][driver][1] != -1:
        switches.append(dp[i][driver][2])
        i = dp[i][driver][1]
        driver = abs(driver-1)
    
    return switches

def j_to_point(dp, switch_points, i):
    minimum = inf
    ind = -1
    original_ind = -1
    for j in range(1, 4):
        if dp[i-j][0][0] < minimum:
            minimum = dp[i-j][0][0]
            ind = i-j
            original_ind = switch_points[i-j]
    
    return [minimum, ind, original_ind]

def m_to_point(dp, switch_points, controls, i):
    minimum = inf
    ind = -1
    original_ind = -1
    for j in range(1, 4):
        if dp[i-j][1][0] + (controls[i] - controls[i-j]) < minimum:
            minimum = dp[i-j][1][0] + (controls[i] - controls[i-j])
            ind = i-j
            original_ind = switch_points[i-j]
    
    return [minimum, ind, original_ind]

def drivers( P, B ):
    P.append((B, True))
    for i in range(len(P)):
        P[i] = (P[i][0], P[i][1], i)
    P.sort(key=lambda x: x[0])

    switch_indices = []
    control = 0
    controls = []
    for i in range(len(P)):
        if not P[i][1]:
            control += 1
        else:
            switch_indices.append(P[i][2])
            controls.append(control)
    
    n = len(switch_indices)
    if n == 0:
        return []
    dp = [[[inf, -1, -1] for _ in range(2)] for _ in range(n)] # wartość, indeks dp przesiadki, indeks oryginalny przesiadki
    dp[0][1][0] = 0
    if n > 1:
        dp[1][1][0] = 0
        dp[1][0] = [controls[1]-controls[0], 0, switch_indices[0]]
    if n > 2:
        dp[2][1][0] = 0
        dp[2][0] = [controls[2] - controls[1], 1, switch_indices[1]]
    

    
    for i in range(3, n):
        dp[i][1] = j_to_point(dp, switch_indices, i)
        dp[i][0] = m_to_point(dp, switch_indices, controls, i)
    
    return get_switches(dp, n)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )