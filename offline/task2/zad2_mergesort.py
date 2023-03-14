from zad2testy import runtests

#Merge Sort
def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    merged = [None]*(n1+n2)

    i1 = i2 = i_merged = 0
    while i1 != n1 and i2 != n2:
        if arr1[i1] > arr2[i2]:
            merged[i_merged] = arr1[i1]
            i1 += 1
            i_merged += 1
        else:
            merged[i_merged] = arr2[i2]
            i2 += 1
            i_merged += 1
    
    while i1 != n1:
        merged[i_merged] = arr1[i1]
        i1 += 1
        i_merged += 1
    while i2 != n2:
        merged[i_merged] = arr2[i2]
        i2 += 1
        i_merged += 1
    
    return merged

def mergesort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = (n-1)//2
    arr1 = mergesort(arr[:mid+1])
    arr2 = mergesort(arr[mid+1:])
    return merge(arr1, arr2)
#End Merge Sort

def snow(S):
    n = len(S)
    S = mergesort(S)
    days_gone = 0
    res = 0
    for i in range(n):
        new_snow = S[i]-days_gone
        if new_snow <= 0:
            break
        res += new_snow
        days_gone += 1
    
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# S = [1, 7, 4, 3, 1]
# S = [0, 0, 0, 11, 14, 2, 3, 0, 0]
# heapsort(S, len(S))
# print(S)
