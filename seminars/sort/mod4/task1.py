#Posortuj tablicę n liczb [0, n^2-1] w czasie liniowym

from random import randrange

def q_sort(A):
    n = len(A)
    C = [0]*n

    for i in range(n):
        C[A[i]%n] += 1
    B = [0]*n
    for i in range(1, n):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        B[C[A[i]%n]-1] = A[i]
        C[A[i]%n] -= 1
    
    for i in range(n):
        A[i] = B[i]
    
    C = [0]*n
    B = [0]*n

    for i in range(n):
        C[A[i]//n] += 1
    
    for i in range(1, n):
        C[i] += C[i-1]
    
    for i in range(n-1, -1, -1):
        B[C[A[i]//n]-1] = A[i]
        C[A[i]//n] -= 1
    
    for i in range(n):
        A[i] = B[i]

if __name__ == "__main__":
    n = 30
    arr = [randrange(0, n^2) for _ in range(n)]

    q_sort(arr)
    print(arr)