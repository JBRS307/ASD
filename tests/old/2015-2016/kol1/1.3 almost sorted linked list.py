"""3. Dana jest struktura Node opisująca listę jednokierunkową:
struct Node { Node * next; int value; };
Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
wejściowej.
"""
class Node:
    def __init__(self):
        self.val = None
        self.next = None


def tab2list(T):
    H = Node()  # wartownik
    C = H
    for i in range(len(T)):
        X = Node()
        X.val = T[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L:
        print(L.val, "->", end=" ")
        L = L.next
    print("|")


def fixSortedList(first):
    warden = Node()
    warden.next = first
    bad = None
    if first.next.val < first.val:
        bad = first
        warden.next = first.next
    else:
        prev = warden
        prev.next = first
        p = first
        while p.next is not None and p.val <= p.next.val:
            prev, p = p, p.next
        if p.next is not None and prev.val <= p.next.val:
            bad = p
            prev.next = p.next
        elif p.next is not None:
            bad = p.next
            p.next = p.next.next
        else:
            return False
    prev = warden
    curr = warden.next
    while curr is not None and curr.val < bad.val:
        prev, curr = curr, curr.next
    prev.next = bad
    bad.next = curr
    return warden.next


T = [1, 2, 0, 4, 5, 6, 7, 8, 9, 10]
L = tab2list(T)
printlist(L)
printlist(fixSortedList(L))
