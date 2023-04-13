#Wstaw liczbę do posortowanej listy jednokierunkowej

class Node:
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val
#=====================================================

def list_insert(head, data):
    p = head
    while (p.next is not None) and \
          (p.next.val < data.val):
          p = p.next
    
    data.next = p.next
    p.next = data

    return head
#-----------------------------------------------------

def del_max(head):
    max_val = 0
    p = head

    while (p is not None) and (p.next is not None):
        max_val = max(max_val, p.val)
        p = p.next
    
    p = head
    if p.val == max_val:
        head = p.next
        del p
        return head
    
    while p.next.val != max_val:
        p = p.next

    p.next = p.next.next
    return head
#-----------------------------------------------------

#Sortowanie listy przez wstawianie (ja pierdole)
def iSort(head): # $3000
    sorted_head = Node()
    while head.next is not None:
        p = head.next
        head.next = head.next.next
        p.next = None
        sorted_head = list_insert(sorted_head, p)
    
    return sorted_head
#=====================================================

if __name__ == "__main__":
    pass
