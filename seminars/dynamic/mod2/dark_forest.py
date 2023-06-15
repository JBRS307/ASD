def dark_forest(arr):
    n = len(arr)
    dp = [[0]*2 for _ in range(n)]

    dp[0][0] = arr[0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][1] + arr[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][1])
    
    # print(*dp, sep="\n", end="\n\n")
    return max(dp[n-1][0], dp[n-1][1])

if __name__ == "__main__":
    print(dark_forest([1, 3, 7, 5, 6, 6, 2]))
    print(dark_forest([1, 10, 1, 1, 10, 1]))