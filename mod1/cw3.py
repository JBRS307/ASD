#Czy są dwa takie indeksy, w POSORTOWANEJ tablicy, takie, że różnica
#liczb na tych indeksach jest równa n

from random import randrange

if __name__ == "__main__":
    n = int(input())

    # arr = [randrange(10, 21) for _ in range(30)]
    arr = [30, 90, 150, 180]
    arr.sort()
    print(*arr)

    i = 0
    j = 1
    leng = len(arr)

    while not(j == leng-1 and i == leng-1):
        if j >= leng:
            print("IMPOSSIBLE")
            break
        if arr[j] - arr[i] < n:
            j += 1
        if arr[j] - arr[i] > n:
            i += 1
        if arr[j] - arr[i] == n:
            print("FOUND")
            print(i, j)
            break
    
    if j == leng-1 and i == leng-1:
        print("IMPOSSIBLE")
