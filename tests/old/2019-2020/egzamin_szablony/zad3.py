from zad3testy import runtests
import math as mt

def insertsort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

def bucketsort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for elem in arr:
        buckets[int(n*elem)].append(elem)
    
    for i in range(n):
        insertsort(buckets[i])
    
    arr.clear()
    for bucket in buckets:
        arr.extend(bucket)

def fast_sort(tab, a):
    arr = []
    for elem in tab:
        arr.append(mt.log(elem, a))
    
    bucketsort(arr)
    for i in range(len(arr)):
        arr[i] = mt.pow(a, arr[i])
    return arr
    

runtests( fast_sort )
