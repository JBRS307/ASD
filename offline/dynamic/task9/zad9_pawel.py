from zad9testy import runtests


def min_cost( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje
    n = len(O)
    inf = float('inf')
    O.append(L-1)
    C.append(0)
    O.append(0)
    C.append(0)
    O, C = zip(*sorted(zip(O, C)))
    cost = [inf] * (n + 2)
    cost[0] = C[0]
    
    def seek(start,table) :
        nonlocal T,O,C
        for i in range(start,n+1) :
            i_dist = O[i]
            for j in range(i+1,n+2) :
                dist = O[j] - i_dist
                if dist > T :
                    break
                table[j] = min(table[j],table[i] + C[j])
    
    seek(0,cost)
    
    jumper = [inf] * (n+2)
    
    output = inf
    
    for i in range(n+1) :
        jumper[i] = cost[i]
        i_cost = cost[i]
        i_dist = O[i]
        for j in range(i+1,n+2) :
            distance = O[j] - i_dist
            if distance > 2*T :
                jumper[j] = inf
                continue
            jumper[j] = i_cost + C[j]
        seek(i,jumper)
        output = min(output,jumper[-1])
    return output
    return -1

runtests(min_cost, all_tests=True)