#Wybór k-tego elementu w czasie O(n) bez ryzyka ukwadratowienia

#Dana jest ablica arr[n] - chcemy znaleźć liczbę, która po posortowaniu byłaby na k-tej pozycji

#1. Podziel arr na ceil(n/5) grup po 5 (ostatnia może mieć mniej elementów).
#2. Dla każdej 5 znajdujemy medianę (dowolną metodą wykona się do w czasie O(1), czyli ostatecznie dla tego kroku jest O(n)).
#3. Rekurencyjnie znajduję medianę z tych median, niech będzie to x.
#4. Wykonaj partition() używając x jako pivot.
#5. Jeśli x jest na pozycji k, to zwróć x (wykorzystanie selecta)

def partition(arr: list, l: int, r: int) -> int:
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

def median_of_medians(arr: list) -> int:
    n = len(arr)
    m = n//5+1
    fives = [[0]*5 for _ in range(m)]
    medians = [0]*m
    k = 0
    for i in range(m-1):
        for j in range(5):
            fives[i][j] = arr[k]
            k += 1
    j = 0
    while k < n:
        fives[m-1][j] = arr[k]
        k += 1
        j += 1
    
    for i in range(m-1):
        medians[i] = select(fives[i], 3, 0, 4)
    medians[m-1] = select(fives[m-1], j//2+1, 0, j-1)
