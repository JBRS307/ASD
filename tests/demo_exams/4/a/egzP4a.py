from egzP4atesty import runtests 

# szukamy najmniejszego elementu większego num
def bin_search(S, num):
    if len(S) == 0:
        S.append(num)
        return

    start = 0
    end = len(S)-1

    if num >= S[end]:
        S.append(num)
        return
    
    while start != end:
        mid = (start+end)//2
        if S[mid] == num:
            return
        if S[mid] < num:
            start = mid+1
        if S[mid] > num:
            end = mid
    S[end] = num

def mosty ( T ):
    T.sort(key=lambda x: x[0])
    for i in range(len(T)):
        T[i] = T[i][1]
    
    S = []
    for i in range(len(T)):
        bin_search(S, T[i])
    
    return len(S)

runtests ( mosty, all_tests=True )