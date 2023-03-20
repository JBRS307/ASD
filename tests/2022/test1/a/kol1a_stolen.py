from kol1atesty import runtests

def hash(s):
    x = 10_002_137
    p = 1_000_000_433

    res = 0
    for c in s:
        res = ((res*x)%p+ord(c))%p

    return res

def mergesort(T):
    if (len(T) == 1): return T

    n = len(T)

    T1 = mergesort(T[:n//2])
    T2 = mergesort(T[n//2:])
    
    i, j = 0, 0
    n1 = len(T1)
    n2 = len(T2)
    ans = []

    while i < n1 and j < n2:
        s1, s1_num = T1[i]
        s2, s2_num = T2[j]
        if s1 == s2:
            ans.append((s1, s1_num+s2_num))
            i += 1
            j += 1
        elif s1 < s2:
            ans.append(T1[i])
            i += 1
        else:
            ans.append(T2[j])
            j += 1

    while i < n1:
        ans.append(T1[i])
        i += 1
    while j < n2:
        ans.append(T2[j])
        j += 1

    return ans

def g(T):
    
    for i in range(len(T)):
        s_rev = T[i][::-1]
        if s_rev < T[i]: T[i] = s_rev
        T[i] = (hash(T[i]), 1)
    #print(T)
    ans = mergesort(T)

    res = -1
    for x, y in ans:
        res = max(res, y)

    return res


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )

#print(g(["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]))
