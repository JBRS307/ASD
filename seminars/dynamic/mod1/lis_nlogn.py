def binary_search(A, val):
    left = 0
    right = len(A) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if val > A[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left

def lis(A):
    n=len(A)
    last=[] 


    for i in range(n):
        idx=binary_search(last,A[i]) 

        if idx == len(last):
            last.append(A[i])
        else:
            last[idx]=A[i] 


    return len(last)


print(lis([3, 1, 5, 7, 2, 4, 9, 3, 17, 3]))