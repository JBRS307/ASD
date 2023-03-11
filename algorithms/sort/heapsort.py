from random import randrange

#funkcje pomocnicze
def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2


#Przywracanie własności kopca
def heapify(arr, i, n):
    l = left(i)
    r = right(i)
    max_index = i

    if l < n and arr[l] > arr[max_index]:
        max_index = l
    if r < n and arr[r] > arr[max_index]:
        max_index = r
    
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, max_index, n)
    return

#Budowanie kopca
def build_heap(arr, n):
    for i in range(parent(n-1), -1, -1):
        heapify(arr, i, n)
    
    return

#Heaposort
def heapsort(arr):
    n = len(arr)
    build_heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return

if __name__ == "__main__":
    n = 30
    k = 100
    arr = [randrange(1, k+1) for _ in range(n)]

    print(*arr)
    heapsort(arr)
    print(*arr)