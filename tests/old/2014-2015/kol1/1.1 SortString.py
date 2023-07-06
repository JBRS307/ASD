"""1. Napisać funkcję: void sortString(string A[]); Funkcja sortuje tablicę n stringów różnej
długości. Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego."""
def SortString(T):
    low, high = float("inf"), float("-inf")
    for x in T:
        z = len(x)
        if z > high:
            high = z
        if z < low:
            low = z
    m = high - low + 1
    n = len(T)
    bucket = [[] for _ in range(m)]
    for i in range(n):
        bucket[len(T[i]) - low] += [T[i]]
    temp = []
    for i in range(m - 1, -1, -1):
        temp = bucket[i] + temp
        countsort(temp, i)
    for i in range(n):
        T[i] = temp[i]


def countsort(A, l):
    n = len(A)
    low, high = float("inf"), float("-inf")
    B = [0] * n
    for x in A:
        low = min(low, ord(x[l]))
        high = max(high, ord(x[l]))
    C = [0] * (high - low + 1)
    for x in A:
        ind = ord(x[l]) - low
        C[ind] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        ind = ord(A[i][l]) - low
        C[ind] -= 1
        B[C[ind]] = A[i]
    for i in range(n):
        A[i] = B[i]


T = ["jajko", 'pisac', 'kkka', 'kkkab', 'majo', 'pinokio', 'abba', 'abbak']
SortString(T)
print(T)
