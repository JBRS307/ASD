#Zrobione mergesortem ze slicingiem, zamiast klasycznej implementacji, ponieważ ta działa szybciej

from kol1atesty import runtests

def calc_hash(s):
    r = ord('a')-1
    p = 10_009
    p_pow = 1
    m = 1_000_009
    res = 0
    for c in s:
        res = (res+(ord(c)-r)*p_pow)%m
        p_pow = (p*p_pow)%m
    return res

#Radix Sort
def radix_count(arr, n, exp):
    count = [0]*10
    res = [0]*n

    for i in range(n):
        num = arr[i]//exp
        count[num%10] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        num = arr[i]//exp
        res[count[num%10]-1] = arr[i]
        count[num%10] -= 1
    
    for i in range(n):
        arr[i] = res[i]

def radixsort(arr, n):
    exp = 1
    for i in range(10):
        radix_count(arr, n, exp)
        exp *= 10


def g(T):
    n = len(T)
    
    for i in range(n):
        temp = T[i][::-1]
        if temp < T[i]:
            T[i] = temp

    T = [calc_hash(s) for s in T]
    radixsort(T, n)

    top_strength = 0
    strength = 1
    for i in range(1, n):
        if T[i] == T[i-1]:
            strength += 1
        else:
            if strength > top_strength:
                top_strength = strength
            strength = 1
    if strength > top_strength:
        top_strength = strength
    
    return top_strength
    #Ostateczna złośoność O(Nlog(N))


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True)

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# print(g(T))
# for i in range(len(T)):
#     temp = T[i][::-1]
#     if temp < T[i]:
#         T[i] = temp
#     T[i] = calc_hash(T[i])
# print(T)
# radixsort(T, len(T))
# print(T)
