from random import randrange
from time import time

def merge(arr, l, m, r):
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

def mergesort(arr, l, r):
    if l < r:
        m = l + (r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)

if __name__ == "__main__":
    arr = [randrange(1, 101) for _ in range(1_000_000)]
    print("Done", end="\n\n")

    start_time = time()
    arr = mergesort(arr, 0, 999_999)
    end_time = time()
    
    print(end_time - start_time)