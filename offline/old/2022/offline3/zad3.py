from zad3testy import runtests

def merge(arr: list, l: int, m: int, r: int) -> None:
    n1 = m-l+1
    n2 = r-m

    arr1 = arr[l:m+1]
    arr2 = arr[m+1:r+1]

    i1 = i2 = 0
    j = l
    while i1 < n1 and i2 < n2:
        if arr1[i1] < arr2[i2]:
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

def mergesort(arr: list, l: int, r: int) -> None:
    if l < r:
        m = l+(r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)

def bucket_sort(arr: list) -> None:
    n = len(arr)
    buckets = [[] for _ in range(n)]

    max_elem = max(arr)
    min_elem = min(arr)

    b_range = (max_elem - min_elem)/n

    if(max_elem - min_elem) == 0:
        for elem in arr:
            buckets[n-1].append(elem)
        mergesort(buckets[n-1], 0, n-1)
        return buckets[n-1]
    
    for elem in arr:
        diff = (elem - min_elem)/b_range - int((elem - min_elem)/b_range)
        if diff < 0.0000001 and elem != min_elem:
            buckets[int((elem - min_elem)/b_range) - 1].append(elem)
        else:
            buckets[int((elem - min_elem)/b_range)].append(elem)
    
    for i in range(n):
        mergesort(buckets[i], 0, len(buckets[i])-1)
    
    i = 0
    for bucket in buckets:
        for elem in bucket:
            arr[i] = elem
            i += 1

def SortTab(T,P):
    bucket_sort(T)
    return T

runtests( SortTab )