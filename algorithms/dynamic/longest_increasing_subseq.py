def lis(arr):
    dp = [0]*len(arr)
    dp[0] = 1

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = dp[j]+1 if dp[j]+1 > dp[i] else dp[i]
            else:
                dp[i] = dp[j] if dp[j] > dp[i] else dp[i]
    
    return dp[len(arr)-1]

if __name__ == "__main__":
    arr = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
    print(lis(arr))