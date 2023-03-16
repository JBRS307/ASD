#Merge Sort
def merge(arr, l, m, r): #l - start 1, r - start2
    n1 = m-l+1
    n2 = r-m
    arr1 = [0]*(n1)
    arr2 = [0]*(n2)

    for i in range(n1):
        arr1[i] = arr[l+i]
    for i in range(n2):
        arr2[i] = arr[m+1+i]
    
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

if __name__ == "__main__":
    arr = [3, 6, 5, 4, 1, 8]
    mergesort(arr, 0, len(arr)-1)
    print(*arr)