from zad3testy import runtests

#Radix Sort
def radix_count(arr, n, exp):
    count = [0]*10
    res = [0]*n

    for i in range(n):
        index = (arr[i]//exp)%10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        index = (arr[i]//exp)%10
        res[count[index]-1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = res[i]

def radixsort(arr, n):
    exp = 1
    max_elem = max(arr)
    while max_elem//exp > 0:
        radix_count(arr, n, exp)
        exp *= 10
    return arr
#End Radix Sort

def calc_hash(s):
    r = ord('a')-1
    p = 31
    p_pow = 1
    m = 1_000_000_009
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
    
    radixsort(arr, n)
    
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

# arr = [randrange(1, 1_000_000_000) for _ in range(10_000)]
# radixsort(arr, 10_000)
# print(arr)

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# print(strong_string(T))
