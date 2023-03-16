#Mamy k posortowanych list, każda n elementowa, trzeba je scalić w jedną
#Zbudować kopiec z pierwszego elementu każdej z tablic
#Albo po prostu zrobić mergesort

from random import randrange

def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    merged = [0]*(n1+n2)

    i1 = i2 = 0
    j = 0
    while i1 < n1 and i2 < n2:
        if arr1[i1] < arr2[i2]:
            merged[j] = arr1[i1]
            i1 += 1
        else:
            merged[j] = arr2[i2]
            i2 += 1
        j += 1
    
    while i1 < n1:
        merged[j] = arr1[i1]
        i1 += 1
        j += 1
    while i2 < n2:
        merged[j] = arr2[i2]
        i2 += 1
        j += 1
    
    return merged

def merge_arrays(arrays):
    k = len(arrays)

    res = arrays[0]
    for i in range(1, k):
        res = merge(res, arrays[i])
    
    return res

if __name__ == "__main__":
    N = 30
    M = 1000
    K = 10
    
    arrays = [[randrange(1, M+1) for _ in range(N)] for _ in range(K)]
    for i in range(K):
        arrays[i].sort()

    print(arrays)
    print("\n")
    print(*merge_arrays(arrays))
