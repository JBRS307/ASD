from zad2testy import runtests

#Quick Sort
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quicksort(arr, l, r):
    if l < r:
        q = partition(arr, l, r)
        quicksort(arr, l, q-1)
        quicksort(arr, q+1, r)
#End Quick Sort


def snow(S):
    n = len(S)
    quicksort(S, 0, n-1)
    days_gone = 0
    res = 0
    for i in range(n):
        new_snow = S[i]-days_gone
        if new_snow <= 0:
            break
        res += new_snow
        days_gone += 1
    
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# S = [1, 7, 4, 3, 1]
# quicksort(S, 0, len(S)-1)
# print(S)
# S = [0, 0, 0, 11, 14, 2, 3, 0, 0]
# heapsort(S, len(S))
# print(S)
