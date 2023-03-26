#Jakub Rekas

#Algorytm działa w czasie O(Nlog(N)) ze względu na porównywanie wyrazów leksykograficznie w algorytmie sortującym
#1. Najpierw należy ustawić każdy wyraz tak, żeby wszystkie wyrazy równoważne były w w tej samej kolejności, tzn. jeśli
#odwrotność i-tego wyrazu jest mniejsza leksykograficznie od tego wyrazu, to należy ten wyraz odrwócić. W ten sposób
#wszystkie wyrazy równoważne będą w tej samej konfiguracji.
#2. Sortujemy tablicę leksykograficznie (zastosowałem do tego klasycznego mergesorta)
#3. Iterujemy po tablicy począwszy od wyrazu z indeksem 1, każdy wyraz porównujemy z poprzednim (dlatego nie można od 0). 
#Jeśli są jednakowe zwiększamy pomocniczą zmienną "strength" o 1. Jeśli nie są jednakowe sprawdzamy czy 
#aktualna siła jest większa od maksymalnej, jeśli tak, to zastępujemy ją "strength".
#Następnie ustawiamy "strength" na 1 niezależnie od wyniku "if'a" (każdy wyraz ma siłę co najmniej 1, ponieważ nie ma wymogu, że
#i != j)
#4. Zwracamy maksymalną siłę.

from zad3testy import runtests

#Merge Sort
def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m

    arr1 = arr[l:m+1]
    arr2 = arr[m+1:r+1]

    i1 = i2 = 0
    j = l
    while i1 < n1 and i2 < n2:
        if arr1[i1] < arr2[i2]:
            arr[j] = arr1[i1]
            i1 += 1
        else:
            arr[j] = arr2[i2]
            i2 += 1
        j += 1
    
    while i1 < n1:
        arr[j] = arr1[i1]
        i1 += 1
        j += 1
    while i2 < n2:
        arr[j] = arr2[i2]
        i2 += 1
        j += 1

def mergesort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)

def strong_string(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i][::-1]
        if temp < arr[i]:
            arr[i] = temp
        
    mergesort(arr, 0, n-1)
    
    top = 0
    strength = 1
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            strength += 1
        else:
            if strength > top:
                top = strength
            strength = 1
    
    return top





# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# print(strong_string(T))
