"""2. Dane są następujące struktury:
struct Node { Node* next; int val; };
struct TwoLists { Node* even; Node* odd; };
Napisać funkcję: TwoLists split(Node* list);
Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste i drugą zawierającą liczby
nieparzyste. Listy nie zawierają wartowników."""
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class TwoLists:
    def __init__(self):
        self.even = None
        self.odd = None

    def __str__(self):
        return str(self.even) + "\n" + str(self.odd)


def Split(first):
    nowa = TwoLists()
    warden = Node()
    warden.next = first
    q = warden
    p = first
    while p is not None:
        if p.val % 2 == 0:
            q.next = p.next
            p.next = nowa.even
            nowa.even = p
            p = q.next
        else:
            q, p = p, p.next
    if first is not None:
        nowa.odd = first
    return nowa
