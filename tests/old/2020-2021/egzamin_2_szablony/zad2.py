from zad2testy import runtests

class Node:
    def __init__(self) -> None:
        self.edges = []
        self.weights = []
        self.ids = []
    
    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)

def summing(root):
    tree_weights = {}
    def rec(node):
        tree_sum = sum(node.weights)
        for i in range(len(node.edges)):
            tree_sum += rec(node.edges[i])
        tree_weights[node] = tree_sum
        return tree_sum
    rec(root)
    return tree_weights

def find_id(root, tree_sum):
    res = -1
    min_diff = float('inf')
    def rec(node):
        nonlocal res, root, tree_sum, min_diff
        for i in range(len(node.edges)):
            diff = abs((tree_sum[root]-tree_sum[node.edges[i]]-node.weights[i])-tree_sum[node.edges[i]])
            if diff < min_diff:
                min_diff = diff
                res = node.ids[i]
        
        for i in range(len(node.edges)):
            rec(node.edges[i])
    
    rec(root)
    return res

def balance( T ):
    tree_weights = summing(T)
    return find_id(T, tree_weights)

    
runtests( balance )


