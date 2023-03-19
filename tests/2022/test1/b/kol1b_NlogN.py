from kol1btesty import runtests

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
        m = l + (r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)
#End Merge Sort

def str_sort(word):
    n = len(word)
    str_arr = [char for char in word]
    mergesort(str_arr, 0, n-1)

    res = ""
    for char in str_arr:
        res += char
    
    return res


def f(T):
    n = len(T)

    for i in range(n): #Posortowanie mergesortem każdego wyrazu - O(Nlog(N))
        T[i] = str_sort(T[i])
    
    mergesort(T, 0, n-1) #Posortowanie mergesortem tablicy - O(nlog(n)) N >= n, zatem sprowadza się do do O(Nlog(N))
    
    top_pop = 0 #maksymalna popularność anagramowa
    pop = 1 #popularność anagramowa wyrazu
    for i in range(1, n): #pętla sprawdzająca czy wyrazy są jednakowe - O(N)
        if T[i] == T[i-1]:
            pop += 1
        else:
            if pop > top_pop:
                top_pop = pop
            pop = 1
    if pop > top_pop:
        top_pop = pop
    
    return top_pop

#Ostateczna złożoność O(Nlog(N) + N + nlog(n)) -> O(Nlog(N)) (po wykluczeniu stałych)



# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )

# T = ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]
# print(f(T))