from egzP2atesty import runtests
from random import randrange

def reindex(n: int, m: int, k: int) -> list:
    new_ind = [0]*n
    curr_k = k+m-1
    start = [0]*m
    end = [0]*m

    elem = 0
    for row in range(m):
        start[row] = elem
        end[row] = elem+(curr_k-1)
        elem += curr_k
        curr_k -= 1
    
    set_people = 0
    curr_row = curr_col = 0
    while set_people < n:
        if start[curr_row] + curr_col <= end[curr_row]:
            new_ind[start[curr_row] + curr_col] = set_people
            set_people += 1
        curr_row += 1
        if curr_row >= m:
            curr_row = 0
            curr_col += 1
    
    return new_ind, end

def rand_partition(arr: list, ind: list, l: int, r: int) -> int:
    new_pivot = randrange(l, r+1)
    arr[ind[r]], arr[ind[new_pivot]] = arr[ind[new_pivot]], arr[ind[r]]
    return partition(arr, ind, l, r)

def partition(arr: list, ind: list, l: int, r: int) -> int:
    pivot = arr[ind[r]][1]
    i = l-1
    for j in range(l, r):
        if arr[ind[j]][1] >= pivot:
            i += 1
            arr[ind[i]], arr[ind[j]] = arr[ind[j]], arr[ind[i]]
    arr[ind[i+1]], arr[ind[r]] = arr[ind[r]], arr[ind[i+1]]
    return i+1

def quickselect(arr: list, ind: list, l: int, r: int, k: int) -> int:
    if l < r:
        m = partition(arr, ind, l, r)
        if m > k: quickselect(arr, ind, l, m-1, k)
        if m < k: quickselect(arr, ind, m+1, r, k)

def zdjecie(T: list, m: int, k: int) -> None:
    n = len(T)
    ind, end = reindex(n, m, k)

    last_end = end[m-1]
    for i in range(m-2, -1, -1):
        quickselect(T, ind, 0, last_end, end[i])
        last_end = end[i]-1



runtests ( zdjecie, all_tests=True )

# T = [ (1001, 154),(1002, 176),(1003, 189),(1004, 165),(1005, 162) ]
# zdjecie(T, 2, 2)
# print(T)