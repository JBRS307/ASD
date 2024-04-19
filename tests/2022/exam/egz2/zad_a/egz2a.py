from egz2atesty import runtests

class Node:
    def __init__(self, max_free: int=0, w_ind: int=None):
        self.max_free= max_free
        self.w_ind = w_ind
        self.left = None
        self.right = None
    
class WarehouseTree:
    def __init__(self, root: Node, T: int):
        self.root = root
        self.T = T # pojemność magazynu
    
    def add_transport(self, transport: int, curr: "Node"=None) -> int:
        if not curr:
            curr = self.root

        if curr.w_ind is not None:
            curr.max_free -= transport
            return curr.w_ind

        if curr.left and curr.left.max_free >= transport:
            warehouse = self.add_transport(transport, curr.left)
            if warehouse != -1:
                if curr.right:
                    curr.max_free = max(curr.left.max_free, curr.right.max_free)
                else:
                    curr.max_free = curr.left.max_free
                return warehouse
        if curr.right and curr.right.max_free >= transport:
            warehouse = self.add_transport(transport, curr.right)
            if warehouse != -1:
                if curr.left:
                    curr.max_free = max(curr.left.max_free, curr.right.max_free)
                else:
                    curr.max_free = curr.right.max_free
                return warehouse
        return -1

def build_tree(A: list[int], T: int) -> WarehouseTree:
    n = len(A)
    node_arr = [Node(T, i) for i in range(n)]
    while n > 1:
        parent_arr = []
        for i in range(0, n, 2):
            parent = Node(T)
            parent.left = node_arr[i]
            if i + 1 < n:
                parent.right = node_arr[i+1]
            parent_arr.append(parent)
        node_arr = parent_arr
        n = len(node_arr)
    
    return WarehouseTree(parent_arr[0], T)


def coal( A, T ):
    tree = build_tree(A, T)
    for transport in A:
        last = tree.add_transport(transport)
    
    return last

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
