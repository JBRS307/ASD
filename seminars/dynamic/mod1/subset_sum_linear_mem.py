def subset_sum(arr: list[int], amount: int) -> bool:
    n = len(arr)
    dp = [False]*(amount+1)
    dp[0] = True
    for i in range(n):
        for j in range(amount, arr[i]-1, -1):
            if dp[j-arr[i]]: dp[j] = True
    return dp[amount]

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    amount = int(input())
    print(subset_sum(arr, amount))