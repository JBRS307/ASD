def lcs(A: list[int], B: list[int]) -> int:
    n = len(A)
    m = len(B)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = dp[i-1][j] if dp[i-1][j] > dp[i][j-1] else dp[i][j-1] # max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]

if __name__ == "__main__":
    A = [3, 2, 1, 0, 5, 10]
    B = [7, 8, 2, 0, 4, 5]


    print(lcs(A, B))
