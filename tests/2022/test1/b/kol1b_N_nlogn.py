from kol1btesty import runtests

def calc_hash(s):
    p = 10_009
    m = 1_000_000_009
    res = 0
    for c in s:
        res = ((res*p)%m+ord(c))%m
    return res
#Sortowanie przez zliczanie jest świetnym wyborem w wypadku sortowania liter w wyrazie, ponieważ można ten problem
#sprowadzić do sortowania tablicy, w której liczby zawierają się w przedziale [1, 26], więc zmienna k zawarta w złożoności
#counting sorta będzie mała.
#Counting Sort
def counting_sort(arr):
    n = len(arr)
    count = [0]*26 #ponieważ tyle jest liter
    reductor = ord('a')
    res = [""]*n

    for char in arr:
        count[ord(char)-reductor] += 1
    
    for i in range(1, 26):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        index = ord(arr[i])-reductor
        res[count[index]-1] = arr[i]
        count[index] -= 1
    
    return res
#End Counting Sort

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

def str_sort(word):
    n = len(word)
    str_arr = [char for char in word]
    
    str_arr = counting_sort(str_arr)

    res = ""
    for char in str_arr:
        res += char
    return res


def f(T):
    n = len(T)

    for i in range(n):
        T[i] = str_sort(T[i])
    
    for i in range(n):
        T[i] = calc_hash(T[i])
    mergesort(T, 0, n-1)

    top_pop = 0
    pop = 1
    for i in range(1, n):
        if T[i] == T[i-1]:
            pop += 1
        else:
            if pop > top_pop:
                top_pop = pop
            pop = 1
    if pop > top_pop:
        top_pop = pop
    
    return top_pop

#Ostateczna złożoność O(NlogN)

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )

# T = ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]
# print(f(T))