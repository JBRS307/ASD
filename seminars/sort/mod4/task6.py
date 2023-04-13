#Mamy tablicę T, n-elementową. x-y jest maksymalne Szukamy x,y € T pod warunkiem, że nie istnieje z€T y < z < x. W O(n).
#Można użyć kubełków

from random import randrange

#Algorytm oczywisty, służy, żeby sprawdzić czy algorytm właściwy działa
def checker(arr: list[int]) -> tuple[int]:
    arr.sort()
    x = y = 0
    max_diff = 0
    for i in range(n-1):
        diff = arr[i+1]-arr[i]
        if diff > max_diff:
            x = arr[i+1]
            y = arr[i]
            max_diff = diff
    return (x, y)

def bucket_find(arr: list[int]) -> tuple[int]:
    n = len(arr)
    buckets = [[] for _ in range(n)]
    min_elem = min(arr)
    b_range = (max(arr) - min_elem)/n

    for elem in arr:
        diff = (elem-min_elem)/b_range - int((elem-min_elem)/b_range)
        if diff < 0.00000001 and elem != min_elem:
            buckets[int((elem-min_elem)/b_range)-1].append(elem)
        else:
            buckets[int((elem-min_elem)/b_range)].append(elem)
    
    max_diff = 0
    x = y = 0
    i, j = 0, 1
    while i < n-1:
        if buckets[i] == []:
            i += 1
            j += 1
            continue

        temp_y = max(buckets[i])
        while buckets[j] == []:
            j += 1
        temp_x = min(buckets[j])
        diff = temp_x - temp_y
        if diff > max_diff:
            x = temp_x
            y = temp_y
            max_diff = diff
        i = j
        j = i+1
    
    return (x, y)

if __name__ == "__main__":
    n = 50
    k = 1500
    arr = [randrange(0, k+1) for _ in range(n)]

    print(bucket_find(arr))
    print(checker(arr))