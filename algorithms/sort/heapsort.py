#funkcje pomocnicze
def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2


#Przywracanie własności kopca
def heapify(arr, i):
    n = len(arr)

    l = left(i)
    r = right(i)
    max_index = i

    if l < n and arr[l] > arr[max_index]:
        max_index = l
    if r < n and arr[r] > arr[max_index]:
        max_index = r
    
    if max_index != i:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, max_index)
    return

#Budowanie kopca
def build_heap(arr):
    n = len(arr)

    for i in range(parent(n-1), -1, -1):
        heapify(arr, i)