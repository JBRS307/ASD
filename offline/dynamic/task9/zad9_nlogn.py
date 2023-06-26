from zad9testy import runtests
from math import inf
from queue import PriorityQueue

def merge_OC(O, C):
    P = []
    for i in range(len(O)):
        P.append((O[i], C[i]))
    return P

def min_cost( O, C, T, L ):
    P = merge_OC(O, C)
    P.append((0, 0))
    P.append((L, 0))
    P.sort()
    n = len(P)
    P[0] = [P[0][0], P[0][1], 0, 0]
    for i in range(1, n):
        P[i] = [P[i][0], P[i][1], None, None]

    Q1 = PriorityQueue() # bez wyjątku
    Q2 = PriorityQueue() # z wykorzystanym wcześniej wyjątkiem
    Q3 = PriorityQueue() # z wyjątkiem, ale jeszcze niewykorzystanym
    Q1.put((0, P[0]))
    Q3.put((0, P[0]))

    for i in range(1, n):
        d = inf
        while d > T<<1:
            cost, parking = Q3.get()
            d = P[i][0]-parking[0]
        
        P[i][3] = cost + P[i][1]
        Q3.put((cost, parking))
        P[1][3] = P[i][3]
        Q2.put((P[i][3], P[i]))

        d = inf
        while d > T:
            cost, parking = Q1.get()
            d = P[i][0]-parking[0]
        
        P[i][2] = cost + P[i][1]
        Q1.put((cost, parking))
        Q1.put((P[i][2], P[i]))
        Q3.put((P[i][2], P[i]))

        d = inf
        while d > T:
            cost, parking = Q2.get()
            d = P[i][0]-parking[0]
        
        P[i][3] = cost + P[i][1]
        Q2.put((cost, parking))
        Q2.put((P[i][3], P[i]))

    return P[n-1][3]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
