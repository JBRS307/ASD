"""1. Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{ Node* next; double value; }
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.
"""
from math import floor
from LinkedList import Node, tab2list, printlist

def buckesort(first):
    p = first
    n = 0
    while p is not None:
        p = p.next
        n += 1
    Bucket = [[None, None] for _ in range(n)]
    warden = Node()
    warden.next = first

    while first is not None:
        x = floor(int(first.val / 10 * n))
        warden.next = first.next
        first.next = Bucket[x][0]
        Bucket[x][0] = first
        first = warden.next

    for i in range(n):
        if Bucket[i][0] is not None:
            Bucket[i] = insertionSort(Bucket[i][0])
    i = 0
    j = 1
    while i < n - 1:
        if Bucket[j][0] is None:
            j += 1
        else:
            Bucket[i][1].next = Bucket[j][0]
            i = j
            j += 1

    return Bucket[0][0]


def insertionSort(head):
    new = None
    curr = head
    while curr is not None:
        next = curr.next
        new = sortedInsert(new, curr)
        curr = next
    tail = new
    while tail.next is not None:
        tail = tail.next
    return new, tail


def sortedInsert(head, new):
    if head is None or head.val >= new.val:
        new.next = head
        head = new
    else:
        curr = head
        while curr.next is not None and curr.next.val < new.val:
            curr = curr.next
        new.next = curr.next
        curr.next = new
    return head


T = [1.5, 2.4, 7.9, 2.3, 5.9, 3.2, 4.6, 4.0, 8.9, 9.5, 6.6, 0.3, 2.3]
L = tab2list(T)
printlist(L)
printlist(buckesort(L))
