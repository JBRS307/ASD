from random import randrange

#Quick Sort
def partition(arr, l, r):
    pivot = arr[r]

    i = l-1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def rand_part(arr, l, r):
    i = randrange(l, r+1)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, l, r)

def quicksort(arr, l, r):
    if l < r:
        q = rand_part(arr, l, r)
        quicksort(arr, l, q-1)
        quicksort(arr, q+1, r)
#End Quick Sort

if __name__ == "__main__":
    arr = [4, 6, 2, 8, 9, 0, 1]
    quicksort(arr, 0, len(arr)-1)
    print(*arr)