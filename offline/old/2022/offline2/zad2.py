from zad2testy import runtests

def prep_data(arr: list, n: int) -> tuple:
    A = [None]*n
    B = [None]*n

    for i in range(n):
        A[i] = (arr[i][0], i)
        B[i] = (arr[i][1], i)
    
    return (A, B)

def merge(arr: list, l: int, m: int, r: int) -> None:
    n1 = m-l+1
    n2 = r-m

    arr1 = arr[l:m+1]
    arr2 = arr[m+1:r+1]

    i1 = i2 = 0
    j = l
    while i1 < n1 and i2 < n2:
        if arr1[i1][0] < arr2[i2][0]:
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

def depth(arr) -> int:
    n = len(arr)
    A, B = prep_data(arr, n)

    mergesort(A, 0, n-1)
    mergesort(B, 0, n-1)

    counting_arr = [0]*n
    curr_start = None
    counter = 1
    for i in range(n):
        counting_arr[A[i][1]] += n-1-i
        if A[i][0] == curr_start:
            counting_arr[A[i][1]] += counter
            counter += 1
        else:
            curr_start = A[i][0]
            counter = 1
    
    start_series = end_series = 0
    series_leng = 1
    i = 0
    while i < n-1:
        if B[i][0] != B[i+1][0]:
            for j in range(start_series, end_series+1):
                counting_arr[B[j][1]] -= (n-series_leng-start_series)
            series_leng = 1
            start_series = end_series = i+1
            i += 1
        else:
            end_series += 1
            series_leng += 1
            i += 1
        
    return max(counting_arr)
    


runtests( depth ) 

# L = [
#      [1, 6],
#      [5, 6],
#      [2, 5],
#      [8, 9],
#      [1, 6],
#      [7, 9],
#      [8, 9]
# ]

# print(depth(L))