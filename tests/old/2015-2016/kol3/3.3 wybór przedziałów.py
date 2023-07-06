def intervals(T):
    n = len(T)
    T.sort(key=lambda x: x[1])
    T.sort(key=lambda x: x[0])
    if T[0][0] != 0:
        return False
    i = 0
    while T[i + 1][0] == 0:
        i += 1
    end = T[i][1]
    while i < n:
        if T[i][0] > end:
            return False
        farest = 0
        while i < n and T[i][0] < end:
            if farest < T[i][1]:
                farest = T[i][1]
            i += 1
        end = farest
        if end == 1:
            return True
    return False


T = [(0.15, 0.2), (0, 0.5), (0.6, 0.8), (0.75, 0.95), (0.85, 1)]
print(intervals(T))
