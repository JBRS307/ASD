from zad2testy import runtests

#Heap Sort
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
    
    return

def build_heap(arr, n):
    for i in range(parent(n-1), -1, -1):
        heapify(arr, i, n)
    return

def heapsort(arr, n):
    build_heap(arr, n)
    days_gone = 0
    res = 0
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        new_snow = arr[i]-days_gone
        if new_snow <= 0:
            break
        res += new_snow
        days_gone += 1
        heapify(arr, 0, i)
    return res
#End Heap Sort


def snow(S):
    n = len(S)
    return(heapsort(S, n))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# S = [1, 7, 4, 3, 1]
# S = [0, 0, 0, 11, 14, 2, 3, 0, 0]
# heapsort(S, len(S))
# print(S)
