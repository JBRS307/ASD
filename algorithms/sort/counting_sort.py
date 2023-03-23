def counting_sort(arr: list) -> None:
    n = len(arr)
    m = max(arr)+1
    count = [0]*(m)
    res = [0]*n

    for i in range(n):
        count[arr[i]] += 1
    
    for i in range(1, m):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        res[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    
    for i in range(n):
        arr[i] = res[i]

if __name__ == "__main__":
    arr = [11, 3, 56, 9, 10]
    counting_sort(arr)
    print(arr)