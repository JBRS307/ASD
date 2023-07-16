# Jakub Rekas

# Na początku trzeba transponować zależności teleportacji. Teraz dla każdej planety wiemy
# SKĄD możemy się do niej teleportować, a to znacznie bardziej przydatna informacja.
# Następnie wykonujemy funkcję f(b, i). Jeśli b == 0 sprawdzamy dodatkowo wszystkie możliwe miejsca, z których możemy się teleportować
# z b = 0.
# następnie wykonujemy rekurencyjnie tę funkcję dla każdej z planet, z których dolecenie na planetę i jest możliwe, sprawdzając wartości
# tylko do maksymalnej ilości paliwa, jakie możemy mieć na każdej z nich. Łatwo to wyliczyć, jest to E pomniejszone o
# dystans między planetą j oraz planetą j-1, można tak robić, ponieważ są posortowane.
# Ponadto jeśli okaże się,
# że dla jakiegoś przypadku dotankowanie na planecie j, żeby osiągnąć b sprawi, że przekroczymy E, to nie
# wykonjemy funkcji dla tej wartości paliwa na j. Wynikiem jest minimum z dolecenia do n-1, dla każdej możliwej wartości b.

#złoźoność rekurencji z memoizacją O(n^2E^2)



from egz1btesty import runtests
inf = float('inf')

def transpone_T(T):
    n = len(T)
    tp_to = [[] for _ in range(n)]
    for i in range(n):
        if T[i][0] != i:
            tp_to[T[i][0]].append((i, T[i][1]))
    
    return tp_to

def flight(D, C, tp_to, E):
    n = len(D)
    memo = [[inf]*(E+1) for _ in range(n)]
    for gas in range(E+1):
        memo[0][gas] = 0

    def f(i, b):
        nonlocal memo, n, tp_to, D, C, E
        if memo[i][b] != inf:
            return memo[i][b]
        if b == 0:
            min_cost = inf
            for j in range(len(tp_to[i])):
                cost = f(tp_to[i][j][0], 0)+tp_to[i][j][1]
                min_cost = min(cost, min_cost)
            memo[i][0] = min_cost
        
        min_cost = inf
        for j in range(i):
            dist = D[i]-D[j]
            if dist > E:
                continue
            if j == 0:
                max_gas = 0
            else:
                max_gas = E - (D[j]-D[j-1])
            for gas in range(max_gas+1):
                # cost = inf
                diff = b-(gas-dist) # paliwo, które trzeba dotankować
                if diff > (E-gas):
                    continue
                if diff >= 0:
                    cost = f(j, gas)+(diff*C[j])
                else:
                    # cost = f(j, gas)
                    continue
                min_cost = min(cost, min_cost)
        memo[i][b] = min(memo[i][b], min_cost)
        return memo[i][b]
    
    min_cost = inf
    max_gas = E-(D[n-1]-D[n-2])
    for i in range(max_gas+1):
        cost = f(n-1, i)
        min_cost = min(cost, min_cost)
    
    return min_cost



def planets( D, C, T, E ):
    tp_to = transpone_T(T)
    return flight(D, C, tp_to, E)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
