from random import randrange

def insertsort(arr: list) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

def bucketsort(arr: list[int]) -> None:
    n = len(arr)
    min_elem = min(arr)
    max_elem = max(arr)
    bucket_range = (max_elem-min_elem)/n
    buckets = [[] for _ in range(n)]

    for elem in arr:
        diff = (elem-min_elem)/bucket_range - int((elem-min_elem)/bucket_range) #część ułamkowa liczby
        if diff < 0.00000001 and elem != min_elem:
            buckets[int((elem-min_elem)/bucket_range)-1].append(elem)
        else:
            buckets[int((elem-min_elem)/bucket_range)].append(elem)
    
    for i in range(n):
        insertsort(buckets[i])
    
    res = []
    for bucket in buckets:
        res += bucket
    
    for i in range(n):
        arr[i] = res[i]

if __name__ == "__main__":
    n = 50
    k1 = 11
    k2 = 131
    arr = [randrange(k1, k2+1) for _ in range(n)]
    # arr[0] = 15
    # arr[1] = 128
    
    print(*arr, end="\n\n")
    print(max(arr), min(arr), end="\n\n")
    bucketsort(arr)
    print(*arr)
