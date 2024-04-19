# Algorytm działa w średnim czasie w O(nlogn), w pesymistycznym O(n^2), bo wtedy trzeba przeglądać za każdym
# razem całe drzewo

# Tworzymy drzewo (takie jak było na wykładzie), które podczepia się pod każdy element tablicy, a wartość w danym
# węźle to suma wartości jego dzieci.
# Dla każdego transportu zachłannie sprawdzamy drzewo od lewej wyszukując pierwszy magazyn, w którym dany transport się
# zmieści. Magazynów jest tyle ile transportów, więc nie będzie sytuacji, że jakiś transport pozostanie bez przydziału.
# W drzewie jest ~2n węzłów.

from egz2atesty import runtests


class Node:
    def __init__(self, free=0, w_ind=None):
        self.right = None
        self.left = None
        self.free = free       # ilość wolnego miejsca, które "widzi" dany węzeł
        self.w_ind = w_ind     # indeks magazynu (mają go tylko liście)

class WarehouseTree:
    def __init__(self, T, root=None):
        self.root = root
        self.T = T # pojemność magazynu
    
    def add_transport(self, transport, curr=None):
        if not curr:
            curr = self.root
        
        if curr.w_ind is not None:
            curr.free -= transport
            return curr.w_ind
        
        if curr.left and curr.left.free >= transport:
            warehouse = self.add_transport(transport, curr.left)
            if warehouse != -1:
                curr.free -= transport
                return warehouse
        if curr.right and curr.right.free >= transport:
            warehouse = self.add_transport(transport, curr.right)
            if warehouse != -1:
                curr.free -= transport
                return warehouse
        return -1

def build_tree(A, T):
    n = len(A)
    node_arr = [Node(T, i) for i in range(n)]
    # while wykona się O(logn) razy, ponieważ długość tablicy parentów zawsze wynosi ceil(n/2)
    # gdzie n to długość tablicy node'ów (dzieci)
    # skoro ilość parentów zmniejsza się dwukrotnie to również for działa w czasie O(logn)
    # cała funkcja działa zatem w czasie O((logn)^2) < O(nlogn)
    while n > 1:
        parent_arr = []
        for i in range(0, n, 2):
            parent = Node()
            parent.left = node_arr[i]
            parent.free += node_arr[i].free
            if i+1 < n:
                parent.right = node_arr[i+1]
                parent.free += node_arr[i+1].free
            parent_arr.append(parent)
        node_arr = parent_arr # przepięcie wskaźnika
        n = len(parent_arr)
    
    tree = WarehouseTree(T, parent_arr[0])
    return tree




def coal( A, T ):
    tree = build_tree(A, T)

    for transport in A:
        last_transport = tree.add_transport(transport)
    
    return last_transport


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )