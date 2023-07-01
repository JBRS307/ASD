from egz1btesty import runtests
from collections import deque

class Node:
    def __init__( self ):
        self.left = None    # lewe poddrzewo
        self.right = None   # prawe poddrzewo
        self.x = None       # pole do wykorzystania przez studentow; robi różne rzeczy
                            # na różnych etapach algorytmu

def count_height(curr, level=0, max_level=0):
    curr.x = level
    max_level = max(level, max_level)
    if curr.left:
        max_level = max(count_height(curr.left, level+1, max_level), max_level)
    if curr.right:
        max_level = max(count_height(curr.right, level+1, max_level), max_level)
    return max_level
    
def BFStree(root, arr):
    q = deque()
    q.append(root)

    while q:
        curr = q.popleft()
        arr[curr.x] += 1
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

def cut_edges_below(curr, end_level, cuts):
    if curr.x == end_level:
        if curr.left:
            left = curr.left
            curr.left = None
            del left
            cuts[0] += 1
        if curr.right:
            right = curr.right
            curr.right = None
            del right
            cuts[0] += 1
        return

    if curr.left:
        cut_edges_below(curr.left, end_level, cuts)
    if curr.right:
        cut_edges_below(curr.right, end_level, cuts)

# Od teraz x będzie zawierał informację o tym
# do jakiego poziomu schodzi drzewo zrootowane w danym wierzchołku
# względem drzewa startowego
def recalc_x(curr, level=0):
    if curr.right is None and curr.left is None:
        curr.x = level
        return level
    
    ll = lr = 0
    new_level = 0
    if curr.right:
        lr = recalc_x(curr.right, level+1)
    if curr.left:
        ll = recalc_x(curr.left, level+1)
    new_level = max(ll, lr)
    curr.x = new_level
    return new_level

def cut_unmatching(curr, good_level, cuts):
    if curr.left:
        if curr.left.x != good_level:
            left = curr.left
            curr.left = None
            del left
            cuts[0] += 1
        else:
            cut_unmatching(curr.left, good_level, cuts)
    if curr.right:
        if curr.right.x != good_level:
            right = curr.right
            curr.right = None
            del right
            cuts[0] += 1
        else:
            cut_unmatching(curr.right, good_level, cuts)

def list_rindex(arr, value):
    return len(arr) - arr[::-1].index(value)-1


def wideentall( T ):
    n = count_height(T)+1
    wide_arr = [0]*n
    BFStree(T, wide_arr)
    max_wide = max(wide_arr)
    max_level = list_rindex(wide_arr, max_wide)
    cuts = [0] # dzięki temu mogę wysyłać do funkcji oryginał, a nie kopię; przekazywany jest wskaźnik
    cut_edges_below(T, max_level, cuts)
    recalc_x(T)
    cut_unmatching(T, T.x, cuts)
    # print(end='')
    return cuts[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )