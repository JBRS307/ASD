#JA PIERDOLĘ

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

#Scala dwie listy
def lmerge(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    head, tail = None, None

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            temp = l1
            l1 = l1.next
        else:
            tmp = l2
            l2 = l2.next

        if tail is None:
            tail = temp
            head = temp
        else:
            tail.next = temp
            tail = tail.next
        tail.next = None
    
    if l1 is not None:
        tail.next = l1
    else:
        tail.next = l2
    
    return head

#wycinanie serii naturalnej z początku listy jednokierunkowej
def cut_sorted_series(l):
    curr = l
    while curr.next is not None and curr.val <= curr.next.val:
        curr = curr.next
    rest = curr.next
    curr.next = None
    return l, rest

#Nie mam bladego pojęcia jak to działa
def list_mergesort(l):
    head = l
    while True:
        l, tail = head, None
        head = None
        counter = 0
        while l is not None:
            s1, l = cut_sorted_series(l)
            if l is None and counter == 0:
                return s1
            counter += 1

            if l is None:
                tail.next = s1
                l = head
                break
            
            s2, l = cut_sorted_series(l)

            merged = lmerge(s1, s2)
            if head is None:
                head = merged
                tail = merged
            else:
                tail.next = merged
            while tail.next is not None: #tail jest ustawiony na koniec dzięki tej pętli
                tail = tail.next

