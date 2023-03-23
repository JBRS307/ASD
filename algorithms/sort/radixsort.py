from random import randrange

#Radix Sort - wersja dla liczb naturalnych (z 0)
def radix_count(arr: list[int], exp: int) -> None:
    n = len(arr)
    count = [0]*10
    res = [0]*n

    for i in range(n):
        index = (arr[i]//exp)%10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        index = (arr[i]//exp)%10
        res[count[index]-1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = res[i]

def radixsort(arr: list) -> None:
    max_elem = max(arr)
    exp = 1
    while max_elem//exp > 0:
        radix_count(arr, exp)
        exp *= 10
#End Radix Sort

if __name__ == "__main__":
    n = 30
    k = 1000
    arr = [randrange(0, k+1) for _ in range(n)]
    print(*arr, end="\n\n")
    radixsort(arr)
    print(*arr, end="\n\n")