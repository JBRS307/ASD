def count_subset_sum(arr: list[int], amount: int) -> bool:
    n = len(arr)
    dp = [[False]*(amount+1) for _ in range(n+1)]
    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(amount+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                need = j-arr[i-1]
                dp[i][j] = dp[i-1][j] or dp[i-1][need]
    
    return dp[n][amount]

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    amount = int(input())
    print(count_subset_sum(arr, amount))