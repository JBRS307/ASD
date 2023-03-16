from zad2testy import runtests

#Merge Sort
def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m
    arr1 = [0]*n1
    arr2 = [0]*n2

    for i in range(n1):
        arr1[i] = arr[l+i]
    for i in range(n2):
        arr2[i] = arr[m+1+i]
    
    i1 = i2 = 0
    j = l
    while i1 < n1 and i2 < n2:
        if arr1[i1] > arr2[i2]:
            arr[j] = arr1[i1]
            i1 += 1
        else:
            arr[j] = arr2[i2]
            i2 += 1
        j += 1
    
    while i1 < n1:
        arr[j] = arr1[i1]
        i1 += 1
        j += 1
    while i2 < n2:
        arr[j] = arr2[i2]
        i2 += 1
        j += 1

def mergesort(arr, l, r):
    if l < r:
        m = l + (r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)
#End Merge Sort

def snow(S):
    n = len(S)
    mergesort(S, 0, n-1)
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
# print(snow(S))
# S = [0, 0, 0, 11, 14, 2, 3, 0, 0]
# heapsort(S, len(S))
# print(S)
