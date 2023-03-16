#Klasyczny quick sort ma rekurencję ogonową, która oddaje sterowanie z powrotem do począktu w następniej instancji
#Rekurencję ogonową można zastąpić pętlą co znacznie zmniejszy zużycie pamięci

#Quick Sort
def partition(arr, l, r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quicksort(arr, l, r):
    while(l < r):
        q = partition(arr, l, r)
        if q-l > r-q:
            quicksort(arr, q+1, r)
            r = q-1
        else:
            quicksort(arr, l, q-1)
            l = q+1
#End Quick Sort

if __name__ == "__main__":
    arr = [4, 6, 2, 8, 9, 0, 1]
    quicksort(arr, 0, len(arr)-1)
    print(*arr)
