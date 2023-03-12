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

def heapify(arr, i, n):
    l = left(i)
    r = right(i)
    max_index = i

    if l < n and arr[l][1] < arr[max_index][1]:
        max_index = l
    if r < n and arr[r][1] < arr[max_index][1]:
        max_index = r
    
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, max_index, n)
    return

def build_heap(arr, n):
    for i in range(parent(n-1), -1, -1):
        heapify(arr, i, n)
    return

def heapsort(arr, n):
    build_heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return
#End of Heapsort

def prettines(n):
    digits = [0]*10
    while n != 0:
        digits[n%10] += 1
        n //= 10
    
    prettines_index = 0
    for dig in digits:
        if dig == 1:
            prettines_index += 1
        elif dig > 1:
            prettines_index -= 1
    return prettines_index

def pretty_sort(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = (arr[i], prettines(arr[i]))
    
    heapsort(arr, n)
    for i in range(n):
        arr[i] = arr[i][0]


if __name__ == "__main__":
    n = 3_000_000
    k = 99999

    arr = gen_data(n, k)
    # arr = [9971, 4889, 8582, 7773, 7932, 2853, 4851, 7912, 5357, 3904, 7210, 4591, 9675, 2290, 7357, 2109, 2879, 3459, \
        #    4178, 5236, 7337, 828, 6552, 6905, 4424, 207, 9144, 7319, 3646, 5255]
    # arr = [1777, 1]
    # print(*arr, end="\n\n")
    start_time = time()
    pretty_sort(arr)
    end_time = time()
    # print(*arr)
    print("Done", end_time-start_time)