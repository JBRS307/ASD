#Mamy dwuwymiarowe pojemniki z wodą i mają dwie współrzędne
#(lewy górny i prawy dolny róg), (p, q) i (u, v)
#są na różnych wysokościach i są połączone
#Do całości nalewamy n litrów wody, ile pojemników jest pełnych?
#Dane w postaci listy krotek [(p, q, u, v), ...]

from random import randrange
from time import time

#Generuje losowo tablicę z danymi, najmniej istotna część kodu
def gen_data(n, k, l):
    arr = [None]*n

    for i in range(n):
        p = randrange(0, k+1)
        v = randrange(0, k+1)

        u = p + randrange(1, l+1)
        q = v + randrange(1, l+1)

        arr[i] = (p, q, u, v)
    
    return arr
#=================================================

#Merge sort działający w miejscu, wolniejszy niż klasyczny, ale złożoność pamięciowa to O(1)
#Merge Sort
def merge(arr, start, mid, end):
    start2 = mid+1

    #Jeśli całość jest już posortowana
    if arr[mid][0] <= arr[start2][0]:
        return
    
    while start <= mid and start2 <= end:
        if arr[start][0] <= arr[start2][0]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            #Przesuwamy wszystkie elementy między start i start2 (bez start2) w prawo
            #Następnie wstawiamy start2 przed start
            while index != start:
                arr[index] = arr[index-1]
                index -= 1
            arr[start] = value

            start += 1
            mid += 1
            start2 += 1
    
    return

def mergesort(arr, l, r):
    if l < r:
        mid = l+(r-l)//2
        mergesort(arr, l, mid)
        mergesort(arr, mid+1, r)
        merge(arr, l, mid, r)
    return
#End Merge Sort

#Funkcja przygotowująca tablice do posortowania.
#Rozdziela dane na 3 tablice, jedna zawiera współrzędne dna, druga sufitu, a 3 informacje o szerokości
#Pierwsze dwie będą sortowane, dlatego ważne jest, żeby każda wartość liczbowa miała przypisany pierwotny indeks, aby można
#było potem łączyć te wartości z powrotem w pary
def prep_data(arr):
    n = len(arr)

    top = [None]*n
    bot = [None]*n
    width = [None]*n
    #0 - lewo, 1 - góra, 2 - prawo, 3 - dół

    for i in range(n):
        top[i] = (arr[i][1], i)
        bot[i] = (arr[i][3], i)
        width[i] = arr[i][2] - arr[i][0]
    
    return top, bot, width

#Główna funkcja zadania
def count_containers(arr, water, n):

    #3 tablice, opisane wcześniej, top i bot zostają posortowane rosnąco
    top, bot, width = prep_data(arr)
    mergesort(top, 0, n-1)
    mergesort(bot, 0, n-1)
    # print(top, end="\n\n")
    # print(bot, end="\n\n")

    full_containers = 0 #Ilość zapełnionych kontenerów
    water_step = 0 #Ilość wody, która w danym kroku jest wlewana do kontenerów
    bot_i = top_i = 0 #Indekys kontenerów, który zostanie otwarty (bot) oraz zamknięty (top) jako następny
    i = bot[0][0] #aktualny poziom wody

    #Pętla wykonuje się, dopóki woda nie osiągnie poziomu najwyższego możliwego sufitu (wtedy wszystkie kontenery będą pełne)
    #lub do momentu, gdy się skończy, przy czym jeśli skończy się i (water == 0), to wtedy, jeśli woda doszła to poziomu, w którym jakiś
    #kontener ma sufit, zostanie on zapełniony
    while i <= top[n-1][0] and water >= 0:
        #Pętle odpowiadają za zamykanie i otwieranie kontenerów, odpowiednio zwiększając lub zmniejszając ilość wlewanej wody
        while bot_i < n and i == bot[bot_i][0]:
            water_step += width[bot[bot_i][1]]
            bot_i += 1
        while top_i < n and i == top[top_i][0]:
            water_step -= width[top[top_i][1]]
            top_i += 1
            full_containers += 1 #Jeśli jakiś kontener zostaje zamknięty znaczy to, że został wypełniony wodą
        
        #Zabezpieczenie przed dużą ilością bezsensownych iteracji w wypadku dużej odległości między kontenerami
        #gdy np jeden kończy się na wysokosći 100, a następny zaczyna dopiero na wysokości 10_000_000 
        if water_step == 0 and bot_i < n:
                i = bot[bot_i][0]
        #Jeśli water_step != 0 skaczemy na następny interesujący 
        #(czyli taki, na którym następuje zmiana wody wlewanej na krok) nas poziom
        elif bot_i < n and top_i < n:
            next_lvl = min(bot[bot_i][0], top[top_i][0])
            water -= water_step*(next_lvl-i)
            i = next_lvl
        elif top_i < n: #To wykonujemy, gdy otworzymy już wszystkie pojemniki
            next_lvl = top[top_i][0]
            water -= water_step*(next_lvl-i)
            i = next_lvl
        else: #Wymagane w ostatniej iteracji, jeśli nie kończy się woda
            i += 1
    
    return full_containers


if __name__ == "__main__":
    n = 3_000_000
    k = 200_000_000 #maksymalne generowanie lewej i dolnej współrzędnej
    l = 40_000_000 #maksymalny rozstrzał pojemnika
    water = 10**18
    arr = gen_data(n, k, l)
    # print(arr)

    start_time = time()
    res = count_containers(arr, water, n)
    end_time = time()

    print(res)
    print(end_time - start_time)

    