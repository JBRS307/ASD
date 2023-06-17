# Jakub Rękas

# Algorytm zachłanny działający w O(n^2). Na początku linearyzujemy sobie tablicę za pomocą
# algorytmu działającego na zasadzie DFSa. Jeśli jakąś plamę jesteśmy w stanie zebrać w kilku miejscach
# to wpisujemy ją w miejscu najwcześniejszego wystąpienia.
# Kiedy tablica jest zlinearyzowana, to sprawdzamy, czy jesteśmy w stanie dojechać z aktualnie posiadaną
# ilością benzyny, jeśli nie, to wyszukujemy największą plamę w zasięgu (licząc od pola startowego).
# Następnie nasz zasięg od pola startowego zwiększamy o pojemność tej plamy i inkrementujemy ilość przystanków
# Jeśli nasz zasięg jest wystarczający, zwracamy ilość przystanków

from zad8testy import runtests

def linearize(T):
    n = len(T)
    m = len(T[0])

    linear_T = [0]*m

    def visit(i, j, value):
        nonlocal n, m, T
        
        value[0] += T[i][j]
        T[i][j] = 0

        if j-1 >= 0 and T[i][j-1]:
            visit(i, j-1, value)
        if j+1 < m and T[i][j+1]:
            visit(i, j+1, value)
        if i-1 >= 0 and T[i-1][j]:
            visit(i-1, j, value)
        if i+1 < n and T[i+1][j]:
            visit(i+1, j, value)
    
    for j in range(m):
        if T[0][j]:
            value = [0] # sztuczka, dzięki której przekazujemy do funkcji oryginał zmiennej, a nie jej kopię
            visit(0, j, value)
            linear_T[j] = value[0]
    return linear_T


def plan(T):
    T = linearize(T)
    n = len(T)

    gas = T[0]
    stops = 1
    while True:
        if gas >= n-1:
            return stops
        max_gas = 0
        max_ind = None
        for i in range(1, gas+1):
            if T[i] > max_gas:
                max_gas = T[i]
                max_ind = i
        gas += max_gas
        T[max_ind] = 0
        stops += 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

