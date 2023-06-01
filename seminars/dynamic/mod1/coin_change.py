def coin_change(coins: list[int], amount: int) -> int:
    coins_size = len(coins)

    dp = [float('inf')]*(amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        ans = float('inf')
        for j in range(coins_size):
            if coins[j] <= i:
                ans = min(ans, dp[i - coins[j]])
            
            if ans != float('inf'):
                dp[i] = ans+1

        
    return -1 if dp[amount] == float('inf') else dp[amount]


if __name__ == "__main__":
    A = [69, 420, 2137]
    T = 69_420

    print(coin_change(A, T))
