# Ten kod to straszny burdel, działa najprawdopodobniej w O(nlogn)
# Najpierw znajduje przedziały bazowe (jest ich co najwyżej 2n) i na ich podstawie tworzy drzewo
# przedziałowe. Atrybuty węzła jak niżej. Parametr snow odpowiada za to ile śniegu leży w punkcie key
# (najwięcej śniegu na pewno będzie na krańcu przedziału bazowego), parametr intervals za to, ile
# przedziałów z I jest ustawionych w danym węźle. Jak już mamy drzewo to wstawiamy przedziały, kiedy przechodzimy
# przez dany węzeł i jego key akurat mieści się w przedziale to zwiększamy snow (ilość śniegu, która tam leży),
# kiedy ustawiamy przedział w węźle to zwiększamy intervals. 
# I teraz ważne. Jeśli ustawawimy jakiś przedział w węźle, który nie jest liściem, to ten śnieg musimy dopisać do wszysktich
# jego dzieci. (np jeśli przedział (3, 10) ustawimy w węźle 5, to do 3, która jest dzieckiem 5 trzeba przekazać informację, że tam spadł śnieg).
# Robimy to na końcu funkcją snow_push, która zwiększa snow dzieci o ilość przedziałów ustawionych w danym węźle.
# Na końcu liniowo przeglądamy drzewo i szukamy największego snow.


from egz3atesty import runtests
from math import inf

class Node:
    def __init__(self, key=None, span=None):
        self.key = key
        self.span = span
        self.left = None
        self.right = None
        self.parent = None
        self.snow = 0
        self.intervals = 0

class IntervalTree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, key, curr=None):
        if not curr:
            curr = self.root
        
        if key < curr.key:
            if curr.left:
                self.insert(key, curr.left)
            else:
                new = Node(key)
                curr.left = new
                new.parent = curr
                new.span = (curr.span[0], curr.key)
        else:
            if curr.right:
                self.insert(key, curr.right)
            else:
                new = Node(key)
                curr.right = new
                new.parent = curr
                new.span = (curr.key, curr.span[1])
        
    def finish(self, curr=None):
        if not curr:
            curr = self.root
        
        if curr.left:
            self.finish(curr.left)
        else:
            curr.left = Node()
            leaf = curr.left
            leaf.parent = curr
            leaf.span = (curr.span[0], curr.key)
        
        if curr.right:
            self.finish(curr.right)
        else:
            curr.right = Node()
            leaf = curr.right
            leaf.parent = curr
            leaf.span = (curr.key, curr.span[1])
    
    def set_single_interval(self, interval, curr=None):
        if not curr:
            curr = self.root
        
        if curr.key == interval[0]:
            curr.snow += 1
            return
        
        if curr.key > interval[0]:
            self.set_single_interval(interval, curr.left)
        elif curr.key < interval[0]:
            self.set_single_interval(interval, curr.right)

    def set_interval(self, interval, cut=None, curr=None):
        if not curr:
            curr = self.root
        if not cut:
            cut = interval

        if curr.key is not None and interval[0] <= curr.key <= interval[1]:
            curr.snow += 1

        if curr.span[0] == cut[0] and curr.span[1] == cut[1]:
            if curr.key is None:
                curr.snow += 1
            curr.intervals += 1
            return

        if curr.key > interval[0]:
            left = curr.left
            self.set_interval(interval, (max(interval[0], left.span[0]), min(interval[1], left.span[1])), curr.left)
        if curr.key < interval[1]:
            right = curr.right
            self.set_interval(interval, (max(interval[0], right.span[0]), min(interval[1], right.span[1])), curr.right)
    
    def push_snow(self, curr=None, push=0):
        if not curr:
            curr = self.root
        
        curr.snow += push
        if curr.left:
            self.push_snow(curr.left, push+curr.intervals)
        if curr.right:
            self.push_snow(curr.right, push+curr.intervals)

    def find_max_snow(self, max_snow, curr=None):
        if not curr:
            curr = self.root

        max_snow[0] = max(max_snow[0], curr.snow)

        if curr.left:
            self.find_max_snow(max_snow, curr.left)
        if curr.right:
            self.find_max_snow(max_snow, curr.right)


def build_tree(tree, base, start, end):
    if start > end:
        return
    mid = (start+end)//2
    # print(start, mid, end)
    tree.insert(base[mid])
    build_tree(tree, base, start, mid-1)
    build_tree(tree, base, mid+1, end)

def init_tree(base):
    n = len(base)
    mid = n//2
    root = base[mid]
    tree = IntervalTree(Node(root, (-inf, inf)))
    build_tree(tree, base, 0, mid-1)
    build_tree(tree, base, mid+1, n-1)
    tree.finish()
    return tree

def find_bases(I):
    intervals = []
    for beg, end in I:
        intervals.extend((beg, end))
    
    intervals = set(intervals)
    return sorted(list(intervals))

def snow( T, I ):
    # print(len(I))
    base = find_bases(I)
    tree = init_tree(base)
    for interval in I:
        if interval[0] == interval[1]:
            tree.set_single_interval(interval)
        else:
            tree.set_interval(interval)
    tree.push_snow()
    max_snow = [0]
    tree.find_max_snow(max_snow)

    return max_snow[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

# T = 100
# I = [(0, 3), (3, 5), (0,3), (3,5), (0,3), (3,5), (5, 10), (20, 30), (25, 35), (26, 26)]
# print(snow(T, I))
