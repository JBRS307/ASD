#Jakub Rękas

#W uproszczeniu, aby otrzymać największą możliwą wartość należy posortować tablicę malejąco i iterować się przez nią
#jednocześnie mając zmienną pomocniczą w postaci ilości minonych dni (należy ją inkrementować co iterację). Liczbę te
#należy każdego dnia odejmować od zebranego śniegu, iterujemy się przez tablicę aż otrzymamy wynik 0(lub mniej), wtedy zrywamy pętlę.

#Działa to, ponieważ każdego dnia topnieje taka sama ilość śniegu, więc najwięcej zbierzemy go wjeżdżając do wąwozów, w których
#jest go najwięcej, NIEZALEŻNIE OD KOLEJNOŚCI (do k pierwszych obszarów w posortowanej tablicy możemy podjechać w dowolnej kolejności
#i dostaniemy tyle samo śniegu). Podjeżdżamy w takiej kolejności, żeby żadnego z tych k pierwszych obszarów nie wyzerować
#W pozostałych obszarach śnieg wyzeruje się zanim zdązymy go zebrać, więc nic nie stracimy przejeżdżając po nim.

#Zadanie można zoptymalizować. Jeśli wykorzystamy heapsorta, który sortuje "od końca" (i.e. jeśli sortujemy rosnąco
#to już po pierwszej iteracji pętli w funkcji heapsort() znamy największy element) to zdobytą ilość śniegu możemy sprawdzać już
#W TRAKCIE sortowania, dzięki czemu kiedy otrzymamy pierwsze 0 możemy przerwać sortowanie. Sortujemy tylko taką część
#tablicy, żeby poznać największą możliwą do zdobycia ilość śniegu co skraca czas wykonywania.

from zad2testy import runtests

#Heap Sort
def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

#z wykładu
def heapify(arr, i, n):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and arr[l] > arr[max_ind]:
        max_ind = l
    if r < n and arr[r] > arr[max_ind]:
        max_ind = r
    
    if max_ind != i:
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
        heapify(arr, max_ind, n)

#z wykładu
def build_heap(arr, n):
    for i in range(parent(n-1), -1, -1):
        heapify(arr, i, n)

#Zmodyfikowany heapsort
def heapsort(arr, n):
    build_heap(arr, n)
    days_gone = 0 #ilość minionych dni
    res = 0 #sumaryczna ilość zebranego już śniegu

    #Pętla musi wykonać się dla 0 (mimo, że tablica jest już wtedy w całości posortowana).
    #Na wypadek, gdyby można było zebrać śnieg z każdego obszaru wąwozu i new_snow nigdzie by się nie wyzerowało
    #dla sortowania nie ma to znaczenia, ponieważ element zamieni się z samym sobą, a w heapify() nic się nie stanie
    #z powodu niespełnienia warunków w instrukcjach if
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        new_snow = arr[i]-days_gone #nowy śnieg otrzymany po wrzuceniu aktualnie największej na "koniec"
        if new_snow <= 0: #Element zrywający pętle, jeśli zbierzemy danego dnia 0 m^3 śniegu, to każdego następnego również, nie ma sensu dalej sortować
            break
        res += new_snow
        days_gone += 1
        heapify(arr, 0, i)
    return res
#End Heap Sort


def snow(S):
    n = len(S)
    return heapsort(S, n)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# S = [1, 7, 4, 3, 1]
# S = [0, 0, 0, 11, 14, 2, 3, 0, 0]
# S = [10, 9, 8, 7]
# print(snow(S))
#10 + 8 + 6 + 4 = 28
# heapsort(S, len(S))
# print(S)
