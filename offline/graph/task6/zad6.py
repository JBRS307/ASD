from zad6testy import runtests

def find_machine(M, worker, machine_assign, machine_checked):
    for machine in M[worker]:
        if not machine_checked[machine]:
            if machine_assign[machine] is None:
                machine_assign[machine] = worker
                return True
    
    for machine in M[worker]:
        if not machine_checked[machine]:
            machine_checked[machine] = True
            if find_machine(M, machine_assign[machine], machine_assign, machine_checked):
                machine_assign[machine] = worker
                return True
    
    return False

def binworker( M ):
    n = len(M)
    res = 0

    machine_assign = [None]*n

    for worker in range(n):
        machine_checked = [False]*n

        if find_machine(M, worker, machine_assign, machine_checked):
            res += 1
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )

# M = [ [ 0, 1, 3],
#     [ 2, 4],
#     [ 0, 2],
#     [ 3 ],
#     [ 3, 2] ]

# print(binworker(M))
