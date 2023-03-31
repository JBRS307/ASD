#Jakub Rękas

#Algorytm działa następująco
#1. Dla każdego przedziału [i, i+p-1] tworzy nową tablicę długości p zawierającą elementy z T (nie tworzy ich naraz, tylko po kolei)
#jest tak dlatego, że partition zmienia tablicę, która jest do niego wysyłana, a tego chcę uniknąć
#2. Dla każdej z tych tablic wykonuję algorytm quickselect(był na wykładzie), który sprawdza, jaka liczba będzie na k-tej pozycji,
#czyli k-1 indeksie po posortowaniu MALEJĄCO (o kierunku sortowania świadczy kierunek nierówności w procedurze partition),
#w skrócie szukam selectem k-tej największej w każdym przedziale
#3. W funkcji ksum chodzi pętla, która na bieząco dodaje do zmiennej wynikowej res wyniki z kolejnych przedziałów.

#Procedura select działa w czasie O(p), wykonuje się co najwyżej n razy, złożoność to czasowa to O(np)
#Złożoność pamięciowa to O(p) - w danym czasie istnieje tablica wielkości p

from kol1testy import runtests
# from random import randrange

def partition(arr, l, r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i+1

# def rand_partition(arr, l, r):
#     p_new = randrange(l, r+1)
#     arr[p_new], arr[r] = arr[r], arr[p_new]
#     return partition(arr, l, r)

def quickselect(arr, k, l, r):
    m = partition(arr, l, r)
    # m = rand_partition(arr, l, r)

    if m == k: return arr[m]
    if m > k: return quickselect(arr, k, l, m-1)
    if m < k: return quickselect(arr, k, m+1, r)


def ksum(T, k, p):
    # addition = p-1

    res = 0
    for i in range(len(T)-(p-1)):
        res += quickselect(T[i:(i+p)], k-1, 0, p-1)
    
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )

# T = [7, 9, 1, 5, 8, 6, 2, 12]
# k = 4
# p = 5
# print(ksum(T, k, p))