"""1. Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n
2
-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A, że:
nX−1
i=0
B[i] ¬
2
Xn−1
i=n
B[i] ¬ ... ¬
nX2−1
i=n2−n
B[i].
Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
oszacować i podać jej złożoność czasową.
"""
def countsort2(A, n):  # opcja na wypadek rozstrzału wartości
    low, high = float("inf"), float("-inf")
    B = [0] * n
    for x in A:
        low = min(low, x[1])
        high = max(high, x[1])
    C = [0] * (high - low + 1)
    for x in A:
        ind = x[1] - low
        C[ind] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        ind = A[i][1] - low
        C[ind] -= 1
        B[C[ind]] = A[i]
    for i in range(n):
        A[i] = B[i]


def SumSort(A, B, n):
    sums = [[i, 0] for i in range(n)]
    for i in range(n * n):
        sums[i // n][1] += A[i]
    countsort2(sums, n)
    print(sums)
    for i in range(n):
        for j in range(n):
            B[i * n + j] = A[(sums[i][0]) * n + j]


A = [1, 654, 23, 634, 543, 1123, 435, 314, 543, 902, 123, 432, 11, 10, 541, 90]
B = [0] * 16
SumSort(A, B, 4)
print(B)
