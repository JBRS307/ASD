# Trzeba sobie zapisać oryginalne indeksy, ze względu na odtwarzanie rozwiązania.
# Trzeba posortować przedziały malejąco ze względu na ich koniec. Jeśli k == 1 to nie ma problemu
# Bierzemy po prostu najdłuższy przedział, w tym wypadku algorytm działa w O(n)
# W pozostałych wypadkach działa w O(n^2). Przedział pod indeksem i traktujemy jako nasz przedział
# bazowy, do którego będziemy odnosić nasze obliczenia. Gdy mamy wybrany przedział, do którego
# w danej iteracji się odnosimy, przeglądamy pozostałe przedziały. Przedział o indeksie j musi mieć
# koniec PÓŹNIEJ niż przedział o indeksie ma początek (oczywiste) oraz musi mieć początek nie później
# niż przedział o indeksie i. Ta zasada jest wprowadzona dlatego, że gdy już znaleźliśmy k przedziałów,
# które spełniają dany warunek, to długość przecięcia jest ustalana jako minimum długości przedziału o
# indeksie i lub bezpośredniego przecięcia i z j. Dzieje się tak, ponieważ przedział o indeksie i
# kończy się najwcześniej ze wszystkich k przedziałów w tej iteracji zewnętrzenego fora, a skoro nie może zaczynać
# się później niż i, to to minimum jest w tym wypadku wynikiem dla całego przecięcia k przedziałów.
# zewnętrzną pętlę wykonujemy dla każdego przedziału.

from zad3testy import runtests

def kintersect( A, k ):
    n = len(A)

    for i in range(n):
        A[i] = (i, A[i][0], A[i][1])
    
    A.sort(key=lambda x: -x[2])

    max_len = -1
    if k == 1:
        res = [None]
        for i in range(n):
            curr_len = A[i][2] - A[i][1]
            if curr_len > max_len:
                max_len = curr_len
                res[0] = A[i][0]
        return res
    
    for i in range(n):
        current = [A[i][0]]
        for j in range(n):
            if i != j and A[j][1] <= A[i][1] < A[j][2]:
                current.append(A[j][0])
                if len(current) == k:
                    leng = min(A[j][2]-A[i][1], A[i][2]-A[i][1])
                    if leng > max_len:
                        max_len = leng
                        res = current.copy()
                    break
    return res

runtests( kintersect )

# A = [(0,4),(1,10),(6,7), (2,8)]
# k = 4
# print(kintersect(A, k))