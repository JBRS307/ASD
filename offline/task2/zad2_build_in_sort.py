from zad2testy import runtests

def snow(S):
    n = len(S)
    S.sort(reverse=True)
    days_gone = 0
    res = 0
    for i in range(n):
        new_snow = S[i]-days_gone
        if new_snow <= 0:
            break
        res += new_snow
        days_gone += 1
    
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# S = [1, 7, 4, 3, 1]
# S = [0, 0, 0, 11, 14, 2, 3, 0, 0]
# heapsort(S, len(S))
# print(S)
