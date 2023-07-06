"""2. Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
int goodThief( int A[], int n );
która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny)."""
def thief(A):
    n = len(A)
    F = [-1] * n
    P = [-1] * n
    F[0] = A[0]
    if A[1] > A[0]:
        F[1] = A[1]
    else:
        F[1] = F[0]
        P[1] = 0
    for i in range(2, n):
        if F[i - 2] + A[i] > F[i - 1]:
            F[i] = F[i - 2] + A[i]
            P[i] = i - 2
        else:
            F[i] = F[i - 1]
            P[i] = i - 1

    def printsolution(i):
        if P[i] != -1:
            printsolution(P[i])
        print(i, end=" ")

    printsolution(P[n - 1])
    print(F[n - 1])


T = [10, 5, 3, 7, 11, 2, 6, 9, 4, 1]
thief(T)
