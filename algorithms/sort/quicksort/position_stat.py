#Znajdowanie w O(n) który element tablicy byłby na k-tej pozycji po posortowaniu

from random import randrange

def partition(arr, l, r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i+1

def select(arr, k, l, r):
    m = partition(arr, l, r)

    if m == k:
        return arr[m]
    if m > k:
        return select(arr, k, l, m-1)
    if m < k:
        return select(arr, k, m+1, r)

if __name__ == "__main__":
    N = 100
    K = 10000
    k = 7

    arr = [randrange(1, K+1) for _ in range(N)]

    print(*arr, end="\n\n")
    print(select(arr, k, 0, N-1), end="\n\n")
    print(*sorted(arr))