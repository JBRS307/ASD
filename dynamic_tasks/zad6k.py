from zad6ktesty import runtests 

def haslo ( S ):
    n = len(S)
    if n == 0:
        return 1
    if "00" in S or S[0] == '0':
        return 0
    
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2 if int(S[0]+S[1]) <= 26 else 1
    for i in range(2, n):
        if S[i] == '0' and int(S[i-1]) > 2:
            return 0
        if S[i] != '0' and S[i-1] != '0' and int(S[i-1]+S[i]) <= 26:
            dp[i] = dp[i-1] + dp[i-2]
        elif S[i] == '0':
            dp[i] = dp[i-2]
        else:
            dp[i] = dp[i-1]
    
    return dp[n-1]

runtests ( haslo )