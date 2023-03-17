#Kolejka priorytetowa z wykorzystaniem kopca maximum

from random import randrange

#Obsługa kolejki priorytetowej
def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(arr, i, n):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and arr[l] > arr[max_ind]:
        max_ind = l
    if r < n and arr[r] > arr[max_ind]:
        max_ind = r
    
    if max_ind != i:
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
        heapify(arr, max_ind, n)

def build_heap(arr, n):
    for i in range(parent(n-1), -1, -1):
        heapify(arr, i, n)

def pop_max(arr, n):
    arr[0], arr[n-1] = arr[n-1], arr[0]
    heapify(arr, 0, n-1)
    return arr[n-1]

def insert(arr, n, data):
    arr[n] = data
    i = n
    p = parent(i)
    while arr[i] > arr[p] and i > 0:
        arr[i], arr[p] = arr[p], arr[i]
        i = p
        p = parent(i)
#Koniec kolejki priorytetowej

if __name__ == "__main__":
    N = 30
    K = 20

    arr = [0]*N
    for i in range(N//2):
        arr[i] = randrange(1, K+1)
    n = N//2

    print(*arr)
    print(*sorted(arr, reverse=True), end="\n\n")
    # print(max(arr))
    build_heap(arr, n)
    print(pop_max(arr, n))
    n -= 1
    insert(arr, n, 25)
    n += 1
    print(pop_max(arr, n))
    n -= 1
    # for i in range(N):
    #     print(pop_max(arr, N-i), end=" ")
    # print()

