from zad1testy import runtests
# from functools import cache

def dynamic(I, x, y):
    result = []
    memo = [False]*len(I)

    # @cache
    def rec(ind, y):
        nonlocal I, result, memo
        point = I[ind][1]
        if memo[ind]:
            return True
        if point == y:
            return True
        return_flag = False
        for i in range(ind, len(I)):
            if I[i][0] == point:
                if rec(i, y):
                    memo[i] = True
                    result.append(I[i][2])
                    return_flag = True
                
        return return_flag
    
    for i in range(len(I)):
        if I[i][0] == x:
            if rec(i, y):
                result.append(I[i][2])

    return list(set(result))

def intuse( I, x, y ):
    for i in range(len(I)):
        I[i] = (I[i][0], I[i][1], i)
    I.sort()

    return dynamic(I, x, y)

    
runtests( intuse )


