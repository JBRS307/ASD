#Jakub Rękas

#Zadanie jest typowym problemem na znalezienie maksymalnego skojarzenia w grafie dwudzielnym, nieważonym
#Algorytm działa następująco
#1. Na początku należy zainicjalizować tablicę, w której każdy indeks odpowiada danej maszynie, a wartość pod tym indeksem to przypisany do
#maszyny pracownik. Wartości na początku ustawiamy na None
#2. Iterujemy przez wszystkich pracowników. W każdej iteracji tworzymy tablicę, w której zapisujemy, które maszyny już przejrzeliśmy w danej
#iteracji. (machine_checked)
#3. Każdemu pracownikowi próbujemy przypisać maszynę. Najpierw sprawdzamy, czy którakolwiek z maszyn, przy których może pracować jest wolna,
#jeśli tak, przypisujemy go do tej maszyny. Jeśli natomiast żadna nie jest wolna, rekurencyjnie sprawdzamy, czy pracownik, który został
#do danej maszyny wpisany wcześniej, może zostać przeniesiony. Tablica machine_checked służy do tego, aby nie sprawdzać maszyny,
#do której pracownik aktualnie jest przypisany.
#4. Jeśli nowemu pracownikowi w danej iteracji udało się przypisać maszynę, to zwiększamy wynik o 1.
#5. Na koniec zwracamy ilość pracowników, którym udało się przypisać maszynę. 


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
