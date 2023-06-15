# Mamy tablicę przedmiotów, każdy przedmiot ma jakąś wagę oraz jakąś wartość
# Mamy plecak o określonej pojemności, zapakuj plecak tak, aby ukraść jak najwięcej.

# Rozwiązanie rekurencyjne
# def knapsack(items, cap, memo, index=0, price=0):
#     if cap == 0 or (index == len(items)-1 and cap > 0):
#         return price
#     if cap < 0:
#         return price-items[index-1][0]
#     return max(knapsack(items, cap-items[index][1], index+1, price+items[index][0]), knapsack(items, cap, index+1, price))

def knapsack(items, cap):
    n = len(items)
    dp = [[0]*(cap+1) for _ in range(n)]

    for i in range(items[0][1], cap+1):
        dp[0][i] = items[0][0]

    for j in range(cap+1):
        for i in range(1, n):
            dp[i][j] = dp[i-1][j]
            if j - items[i][1] >= 0:
                if j - items[i][1] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-items[i][1]]+items[i][0])
    
    return dp[n-1][cap]


if __name__ == "__main__":
    shelf = [(14, 3), (25, 10), (1, 10), (32, 32), (11, 10)] # (wartość, waga)
    cap = 20

    print(knapsack(shelf, cap))