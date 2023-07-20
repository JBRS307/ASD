from egz1btesty import runtests
inf = float('inf')

def planets(D, C, T, E):
    n = len(D)
    dp = [[inf]*(E+1) for _ in range(n)]
    dp[0][0] = 0

    for i in range(n):
        if i > 0:
            dist = D[i] - D[i-1]
        else:
            dist = 0
        
        if i > 0:
            dp[i][0] = min(dp[i][0], dp[i-1][dist])
        
        for b in range(1, E+1):
            dp[i][b] = min(dp[i][b], dp[i][b-1]+C[i])

            if i > 0 and b+dist <= E:
                dp[i][b] = min(dp[i][b], dp[i-1][b+dist])
            tp_dest, tp_cost = T[i]
            dp[tp_dest][0] = min(dp[tp_dest][0], dp[i][0]+tp_cost)
    
    return dp[n-1][0]

runtests(planets, all_tests=True)