#Zrobione mergesortem ze slicingiem, zamiast klasycznej implementacji, ponieważ ta działa szybciej

from kol1atesty import runtests
def calc_hash(s):
    r = ord('a')-1
    p = 31
    p_pow = 1
    m = 1_000_000+9
    hash_val = 0
    for c in s:
        hash_val = (hash_val+(ord(c)-r)*p_pow)%m
        p_pow = (p*p_pow)%m
    return hash_val
#Merge Sort
def merge(arr, hash_arr, l, m, r):
    n1 = m-l+1
    n2 = r-m

    arr1 = arr[l:m+1]
    arr2 = arr[m+1:r+1]
    hash1 = hash_arr[l:m+1]
    hash2 = hash_arr[m+1:r+1]

    i1 = i2 = 0
    j = l
    while i1 < n1 and i2 < n2:
        if hash1[i1] < hash2[i2]:
            arr[j] = arr1[i1]
            hash_arr[j] = hash1[i1]
            i1 += 1
        else:
            arr[j] = arr2[i2]
            hash_arr[j] = hash2[i2]
            i2 += 1
        j += 1
    
    while i1 < n1:
        arr[j] = arr1[i1]
        hash_arr[j] = hash1[i1]
        i1 += 1
        j += 1
    while i2 < n2:
        arr[j] = arr2[i2]
        hash_arr[j] = hash2[i2]
        i2 += 1
        j += 1

def mergesort(arr, hash_arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergesort(arr, hash_arr, l, m)
        mergesort(arr, hash_arr, m+1, r)
        merge(arr, hash_arr, l, m, r)
#End Merge Sort

def g(T):
    n = len(T)
    
    for i in range(n):
        temp = T[i][::-1]
        if temp < T[i]:
            T[i] = temp

    hash_T = [calc_hash(s) for s in T]
    mergesort(T, hash_T, 0, n-1)

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
