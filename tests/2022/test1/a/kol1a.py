#Zrobione mergesortem ze slicingiem, zamiast klasycznej implementacji, ponieważ ta działa szybciej

from kol1atesty import runtests

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
#End Merge Sort

def check_palindrome(word):
    n = len(word)
    word = "^" + word + "$"
    if n%2 == 1:
        m = n//2 +1
        radius = 1
        while word[m+radius] == word[m-radius]:
            radius += 1
        radius -= 1
        return 2*radius+1 == n
    else:
        m1 = n//2
        m2 = m1+1
        radius = 0
        while word[m1-radius] == word[m2+radius]:
            radius += 1
        return 2*radius == n


def g(T):
    n = len(T)
    rev_T = [""]*n #O(n)

    for i in range(n): #O(N)
        rev_T[i] = T[i][::-1]
    
    T = T+rev_T

    mergesort(T, 0, (2*n)-1) #O(2nlog(2n)), bo wykluczeniu stałej O(nlog(n))

    top_strength = 0
    strength = 1
    for i in range(1 ,2*n):
        if T[i] == T[i-1]:
            strength += 1
        else:
            if check_palindrome(T[i-1]): #W najgorszym przypadku odpalimy to n razy czyli O(N) w sumie
                strength //= 2
            if strength > top_strength:
                top_strength = strength
            strength = 1
    
    return top_strength
    #Ostateczna złośoność O(N+nlog(n))


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True)

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# print(g(T))
