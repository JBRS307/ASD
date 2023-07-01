from egz2atesty import runtests

def coal( A, T ):
    W = [T]

    last_transport = 0
    for transport in A:
        for i in range(len(W)):
            if transport <= W[i]:
                W[i] -= transport
                last_transport = i
                break
        else:
            last_transport = len(W)
            W.append(T-transport)
    
    return last_transport

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
