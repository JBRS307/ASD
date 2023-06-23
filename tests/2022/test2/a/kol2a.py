from kol2atesty import runtests
from math import inf

def save_indexes(P):
    for i in range(len(P)):
        P[i] = (P[i][0], P[i][1], i)

def extract_switch(P):
    cost = 0
    S = []
    for i in range(len(P)):
        if P[i][1]:
            S.append((P[i][0], cost, P[i][2]))
            cost = 0
        else:
            cost += 1
    return S

def drivers( P, B ):
    P.append((B, True))
    save_indexes(P)
    P.sort()
    S = extract_switch(P)
    # print(S)

    stamina_M = 3
    stamina_J = 2

    switches = []
    n = len(S)
    dp = [[[inf, []] for _ in range(2)] for _ in range(n)]
    dp[0][1][0] = 0 # 0 - Marian, 1 - Jacek

    for i in range(1, n):
        if stamina_J > 0:
            if dp[i-1][1][0] < dp[i-1][0][0]:
                dp[i][1][0] = dp[i-1][1][0]
                dp[i][1][1].extend(dp[i-1][1][1])
                stamina_J -= 1
            else:
                dp[i][1][0] = dp[i-1][0][0]
                dp[i][1][1].extend(dp[i-1][0][1])
                dp[i][1][1].append(S[i-1][2])
                # switches.append((S[i-1][2], i))
                stamina_J = 2
        else:
            dp[i][1][0] = dp[i-1][0][0]
            dp[i][1][1].extend(dp[i-1][0][1])
            dp[i][1][1].append(S[i-1][2])
            # switches.append((S[i-2][2], i))
            stamina_J = 2
        if stamina_M > 0:
            if dp[i-1][0][0] < dp[i-1][1][0]:
                dp[i][0][0] = dp[i-1][0][0]+S[i][1]
                dp[i][0][1].extend(dp[i-1][0][1])
                stamina_M -= 1
            else:
                dp[i][0][0] = dp[i-1][1][0]+S[i][1]
                dp[i][0][1].extend(dp[i-1][1][1])
                dp[i][0][1].append(S[i-1][2])
                # switches.append((S[i-1][2], i))
                stamina_M = 2
        else:
            dp[i][0][0] = dp[i-1][1][0]+S[i][1]
            dp[i][0][1].extend(dp[i-1][1][1])
            dp[i][0][1].append(S[i-1][2])
            # switches.append((S[i-1][2], i))
            stamina_M = 2

    print(end='')

    if dp[n-1][0][0] < dp[n-1][1][0]:
        return dp[n-1][0][1]
    else:
        return dp[n-1][1][1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )