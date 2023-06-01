from math import inf

def chess_board(T):
    n = len(T)
    dp = [[inf for i in range(n)] for j in range(n)]

    dp[0][0] = T[0][0]
    for i in range(n):
        for j in range(n):
            if i-1 >= 0 and dp[i-1][j] < dp[i][j]:
                dp[i][j] = dp[i-1][j]
            if j-1 >= 0 and dp[i][j-1] < dp[i][j]:
                dp[i][j] = dp[i][j-1]

        dp[i][j] += T[i][j]


    return dp[n-1][n-1]