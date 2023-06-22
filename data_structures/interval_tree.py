from math import inf
from collections import deque

class TreeNode:
    def __init__(self, key=None, span=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.span = span
        self.intervals = []

class IntervalTree:
    def __init__(self, root):
        self.root = root
        self.complete = False
    
    def search(self, key):
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr
        return None


    def search_intervals(self, key):
        intervals = []
        stack = deque()

        def find_nodes(curr):
            nonlocal stack, intervals, key
            stack.append(curr)
            if curr.key is None:
                return
            if key < curr.key:
                find_nodes(curr.left)
            elif key > curr.key:
                find_nodes(curr.right)
            else:
                find_nodes(curr.left)
                find_nodes(curr.right)
        
        find_nodes(self.root)

        while stack:
            node = stack.pop()
            intervals.extend(node.intervals)
        
        return intervals

    def set_interval(self, interval: "tuple[int, int]", cut=None, curr=None):
        if curr is None:
            curr = self.root
        if cut is None:
            cut = interval

        if curr.span[0] == cut[0] and curr.span[1] == cut[1]:
            curr.intervals.append(interval)
            return
        
        if curr.key > interval[0]:
            left = curr.left
            self.set_interval(interval, (max(interval[0], left.span[0]), min(interval[1], left.span[1])), curr.left)
        if curr.key < interval[1]:
            right = curr.right
            self.set_interval(interval, (max(interval[0], right.span[0]), min(interval[1], right.span[1])), curr.right)
    
    def insert(self, key, curr=None):
        if curr is None:
            curr = self.root
        
        if key < curr.key:
            if curr.left:
                self.insert(key, curr.left)
            else:
                new = TreeNode(key)
                curr.left = new
                new.parent = curr
                new.span = (curr.span[0], curr.key)
        else:
            if curr.right:
                self.insert(key, curr.right)
            else:
                new = TreeNode(key)
                curr.right = new
                new.parent = curr
                new.span = (curr.key, curr.span[1])

    def finish(self, curr=None):
        if curr is None:
            if self.complete:
                return
            self.complete = True
            curr = self.root
        
        if curr.left:
            self.finish(curr.left)
        else:
            curr.left = TreeNode()
            leaf = curr.left
            leaf.parent = curr
            leaf.span = (curr.span[0], curr.key)
        if curr.right:
            self.finish(curr.right)
        else:
            curr.right = TreeNode()
            leaf = curr.right
            leaf.parent = curr
            leaf.span = (curr.key, curr.span[1])

    def unfinish(self, curr=None):
        if curr is None:
            if not self.complete:
                return
            self.complete = False
            curr = self.root
        
        if curr.left.key is None:
            del curr.left
            curr.left = None
        else:
            curr.intervals = []
            self.unfinish(curr.left)
        
        if curr.right.key is None:
            del curr.right
            curr.right = None
        else:
            curr.intervals = []
            self.unfinish(curr.right)

if __name__ == "__main__":
    arr = [0, 5, 7, 10, 12, 15, 20]

    first = TreeNode(10, (-inf, inf))

    tree = IntervalTree(first)
    tree.insert(5)
    tree.insert(15)
    tree.insert(7)
    tree.insert(0)
    tree.insert(12)
    tree.insert(20)

    tree.finish()
    print()

    # tree.set_interval((0, 5))
    tree.set_interval((5, 20))
    tree.set_interval((7, 12))
    tree.set_interval((10, 15))

    print(tree.search_intervals(12))
    print()
    # tree.unfinish()
    print()




