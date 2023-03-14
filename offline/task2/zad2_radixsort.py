from zad2testy import runtests

def counting_sort(arr, exp):
    n = len(arr)
    res = [0]*n
    count = [0]*10

    for i in range(n):
        count[(arr[i]//exp)%10] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        index = arr[i]//exp
        res[count[index%10]-1] = arr[i]
        count[index%10] -= 1
    
    for i in range(n):
        arr[i] = res[i]

def radixsort(arr):

    max_elem = max(arr)

    exp = 1
    while max_elem//exp != 0:
        counting_sort(arr, exp)
        exp *= 10


def snow(S):
    n = len(S)
    radixsort(S)
    days_gone = 0
    res = 0
    for i in range(n-1, -1, -1):
        new_snow = S[i]-days_gone
        if new_snow <= 0:
            break
        res += new_snow
        days_gone += 1
    
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# S = [1, 7, 4, 3, 1]
# radixsort(S)
# print(S)
# S = [0, 0, 0, 11, 14, 2, 3, 0, 0]
# heapsort(S, len(S))
# print(S)
