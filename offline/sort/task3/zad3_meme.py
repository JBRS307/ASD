from zad3testy import runtests

def strong_string(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i][::-1]
        if temp < arr[i]:
            arr[i] = temp
        
    arr.sort()

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
