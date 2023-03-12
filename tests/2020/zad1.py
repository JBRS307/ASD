from random import randrange
from time import time

def gen_data(n, k):
    return [randrange(1, k+1) for _ in range(n)]
#======================================================
#Heapsort
def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(arr, i, n, sort_by):
    l = left(i)
    r = right(i)
    max_index = i

    if l < n and arr[l][sort_by] < arr[max_index][sort_by]:
        max_index = l
    if r < n and arr[r][sort_by] < arr[max_index][sort_by]:
        max_index = r
    
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, max_index, n, sort_by)
    return

def build_heap(arr, n, sort_by):
    for i in range(parent(n-1), -1, -1):
        heapify(arr, i, n, sort_by)
    return

def heapsort(arr, n, sort_by):
    build_heap(arr, n, sort_by)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i, sort_by)
    return
#End of Heapsort

def prettines(n):
    digits = [0]*10
    while n != 0:
        digits[n%10] += 1
        n //= 10
    
    single = multi = 0
    for dig in digits:
        if dig == 1:
            single += 1
        elif dig > 1:
            multi -= 1
    return single, multi

def pretty_sort(arr):
    n = len(arr)
    for i in range(n):
        single, multi = prettines(arr[i])
        arr[i] = (arr[i], single, multi)
    
    #1 - single, 2 - multi
    heapsort(arr, n, 1)

    # res = [0]*n
    i = 0
    res_ind = 0
    while i < n:
        j = i+1
        new_len = 1
        while j < n and arr[j][1] == arr[i][1]:
            j += 1
            new_len += 1
        temp = [None]*new_len
        for k in range(new_len):
            temp[k] = arr[i]
            i += 1
        heapsort(temp, new_len, 2)
        for k in range(new_len):
            arr[res_ind] = temp[k][0]
            res_ind += 1

    return


if __name__ == "__main__":
    n = 3_000_000
    k = 10**15

    arr = gen_data(n, k)
    # arr = [9971, 4889, 8582, 7773, 7932, 2853, 4851, 7912, 5357, 3904, 7210, 4591, 9675, 2290, 7357, 2109, 2879, 3459, \
        #    4178, 5236, 7337, 828, 6552, 6905, 4424, 207, 9144, 7319, 3646, 5255]
    # print(*arr, end="\n\n")
    start_time = time()
    pretty_sort(arr)
    end_time = time()
    # print(*arr)
    print("Done", end_time-start_time)