from random import uniform

def insertsort(arr: list) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

#Kubełków może być mniej niż n, ale musi to być funkcja liniowa n, a*n, np 0.5n
#Działa dla liczb z zakrezu [0,1)
def bucketsort(arr: list) -> None:
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for elem in arr:
        buckets[int(n*elem)].append(elem)

    for i in range(n):
        insertsort(buckets[i])
    
    res = []
    for bucket in buckets:
        res.extend(bucket)
    
    for i in range(n):
        arr[i] = res[i]


if __name__ == "__main__":
    n = 30
    arr = [0]*n

    for i in range(n):
        elem = uniform(0, 1)
        while elem == 1:
            elem = uniform(0, 1)
        arr[i] = elem
    
    for elem in arr:
        print("%.2f" %elem, end=' ')
    print()

    bucketsort(arr)

    for elem in arr:
        print("%.2f" %elem, end=' ')
    print()