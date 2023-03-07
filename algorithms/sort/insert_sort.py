def insert_sort(arr):
    leng = len(arr)
    
    for i in range(leng):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    
    print(arr)

if __name__ == "__main__":
    arr = [2, 4, 3, 1, 9, 0, 11, 1]

    insert_sort(arr)