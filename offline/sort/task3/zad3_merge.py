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

def calc_hash(s):
    r = ord('a')-1
    p = 31
    p_pow = 1
    m = 1_000_009
    res = 0
    for c in s:
        res = (res + (ord(c)-r)*p_pow)%m
        p_pow = (p*p_pow)%m
    return res

def strong_string(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i][::-1]
        if temp < arr[i]:
            arr[i] = temp
    
    for i in range(n):
        arr[i] = calc_hash(arr[i])
    
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
