# Drzewo BST - bez powtórzeń kluczy

class BSTNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.right = None
        self.left = None
        self.parent = None

class BST:
    def __init__(self, root_node):
        self.root = root_node
        # self.level = 0
    
    def insert(self, key, data):
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left:
                    curr = curr.left
                else:
                    new = BSTNode(key, data)
                    curr.left = new
                    new.parent = curr
                    return
            elif key > curr.key:
                if curr.right:
                    curr = curr.right
                else:
                    new = BSTNode(key, data)
                    curr.right = new
                    new.parent = curr
                    return
            else:
                curr.data = data
                return
    # zwraca wskaźnik na węzeł o zadanym kluczu
    def search(self, key):
        curr = self.root
        while curr:
            if curr.key == key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None
    
    def pred(self, key):
        curr = self.search(key)
        if curr.left is None:
            parent = curr.parent
            while parent and curr.key == parent.left.key:
                curr = parent
                parent = curr.parent
            if parent and curr.key == parent.right.key:
                return parent
            return None
        else:
            curr = curr.left
            while curr.right:
                curr = curr.right
            return curr
    
    def succ(self, key):
        curr = self.search(key)
        if curr.right is None:
            parent = curr.parent
            while parent and curr.key == parent.right.key:
                curr = parent
                parent = curr.parent
            if parent and curr.key == parent.left.key:
                return parent
            return None
        else:
            curr = curr.right
            while curr.left:
                curr = curr.left
            return curr
    
    def min_key(self):
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr
    
    def max_key(self):
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr
    
    def remove(self, key):
        curr = self.search(key)

        if curr.left is None:
            parent = curr.parent
            if curr.key == parent.left.key:
                parent.left = curr.right
            else:
                parent.right = curr.right
            data = curr.data
            del curr
            return data
        elif curr.right is None:
            parent = curr.parent
            if curr.key == parent.left.key:
                parent.left = curr.left
            else:
                parent.right = curr.left
            data = curr.data
            del curr
            return data
        else:
            succ = self.succ(curr.key)
            parent = succ.parent
            parent.left = succ.right

            data = curr.data
            curr.key = succ.key
            curr.data = succ.data
            del succ
            return data
    

if __name__ == "__main__":
    root = BSTNode(10, 13)

    tree = BST(root)
    for i in range(10):
        tree.insert(i, i+15)
    
    for i in range(11, 21):
        tree.insert(i, i+15)
    
    print(tree.succ(9).key)



