from kolutesty import runtests


def ice_cream(T):
    n = len(T)
    maximum = max(T)
    res = 0
    diff = [0]*n

    for i in range(n):
        diff[i] = T[i]-maximum
    
    for i in range(n):
        res += max(0, T[i]+diff[i])
    return res



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = False )
