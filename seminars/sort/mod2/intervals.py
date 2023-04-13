#Zbiór przedziałów domkniętych [a_i, b_i]
#Znajdź przedział, który zawiera najwięcej z pozostałych

from random import randrange

#Funkcja rozdziela tablicę na dwie podtablicę, (x, i), gdzie x = a lub x = b, a jest równe indeksowi
#odcinka, w ten sposób będzie można skojarzyć ze sobą odcinki po posortowaniu tablic
def prep_data(arr):
    n = len(arr)
    A = [None]*n
    B = [None]*n

    for i in range(n):
        A[i] = (arr[i][0], i)
        B[i] = (arr[i][1], i)
    
    return A, B

#Merge Sort
def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    merged = [None]*(n1+n2)

    i1 = i2 = i_merged = 0
    while n1 != 0 and n2 != 0:
        if arr1[i1][0] <= arr2[i2][0]:
            merged[i_merged] = arr1[i1]
            i1 += 1
            n1 -= 1
        else:
            merged[i_merged] = arr2[i2]
            i2 += 1
            n2 -= 1
        i_merged += 1
    
    if n1 == 0:
        while n2 != 0:
            merged[i_merged] = arr2[i2]
            i2 += 1
            i_merged += 1
            n2 -= 1
    if n2 == 0:
        while n1 != 0:
            merged[i_merged] = arr1[i1]
            i1 += 1
            i_merged += 1
            n1 -= 1
    
    return merged

def mergesort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = (n-1)//2
    arr1 = mergesort(arr[:mid+1])
    arr2 = mergesort(arr[mid+1:])
    arr = merge(arr1, arr2)
    return arr
#Koniec Merge Sort

#Rozwiązanie główne
def find_intervals(arr):
    n = len(arr)
    A, B = prep_data(arr)
    A = mergesort(A)
    B = mergesort(B)

    # print(arr, end="\n\n")
    # print(A, end="\n\n")
    # print(B, end="\n\n")
    

    #Po posortowaniu tablic dla każdego odcinka zliczamy ile odcinków ma w tym samym miejscu lub później początek, i liczbę te dodajemy
    #do odpowiedniego indeksu w tablicy zliczającej
    counting_arr = [0]*n
    curr_start = None
    counter = 1
    for i in range(n):
        counting_arr[A[i][1]] += n-1-i
        if A[i][0] == curr_start:
            counting_arr[A[i][1]] += counter
            counter += 1
        else:
            curr_start = A[i][0]
            counter = 1
        
    
    #Następnie liczymy, dla każdego odcinka, ile odcinków ma koniec później niż aktualnie sprawdzany odcinek.
    #Musimy wziąć pod uwagę, że kilka odcinków może kończyć się w tym samym miejscu, do tego służą zmienne curr_end i counter
    #które są wykorzystane do tego, aby do aktualnego odcinka dodać to, co zostało wcześniej odjęte, ponieważ stoi na późniejszej pozycji
    curr_end = None
    counter = 1
    for i in range(n-1, -1, -1):
        counting_arr[B[i][1]] -= n-1-i
        if B[i][0] == curr_end:
            counting_arr[B[i][1]] += counter
            counter += 1
        else:
            curr_end = B[i][0]
            counter = 1
    

    #Szukamy największego elementu w tablicy zliczającej oraz, przede wszystkim, jego indeksu
    max_elem = 0
    max_index = 0
    for i in range(n):
        if counting_arr[i] > max_elem:
            max_elem = counting_arr[i]
            max_index = i
    
    #Gdy mamy maksymalny indeks przeszukujemy tablice A i B w celu znalezienia wartości, które mu odpowiadają,
    #następnie łączymy dwie wartości w parę i zwracamy to jako krotkę.
    a = b = 0
    for i in range(n):
        if A[i][1] == max_index:
            a = A[i][0]
            break
    for i in range(n):
        if B[i][1] == max_index:
            b = B[i][0]
            break
    
    # print(*counting_arr, end="\n\n")
    return (a, b)


def generate_data(n, k):
    arr = [None]*n
    for i in range(n):
        a = randrange(-k, k)
        b = randrange(a+1, k+1)
        arr[i] = (a, b)
    return arr

if __name__ == "__main__":
    n = 10000000
    k = 700
    # arr = generate_data(n, k)
    # print(*arr)

    arr = generate_data(n, k)
    # print(*arr)
    # print()
    # arr = mergesort(arr)
    # print(*arr)

    res = find_intervals(arr)
    # arr = mergesort(arr)

    # print(*arr, end="\n\n")
    print(res)