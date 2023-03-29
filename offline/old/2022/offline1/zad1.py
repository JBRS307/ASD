from zad1testy import Node, runtests

def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

def heapify(arr, i, n):
    l = left(i)
    r = right(i)
    min_ind = i

    if l < n and arr[l].val < arr[min_ind].val: min_ind = l
    if r < n and arr[r].val < arr[min_ind].val: min_ind = r

    if min_ind != i:
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
        heapify(arr, min_ind, n)

def build_heap(arr, n):
    for i in range(parent(n), -1, -1):
        heapify(arr, i, n)




def SortH(p,k):
    heap_size = k+1
    inf_node = Node()
    inf_node.val = float('inf')
    heap = [inf_node for _ in range(heap_size)]

    curr_elem = p

    for i in range(heap_size):
        heap[i] = curr_elem
        curr_elem = curr_elem.next
        if curr_elem is None: break;

    build_heap(heap, heap_size)
    sentry = Node()
    tail = sentry

    while curr_elem is not None:
        tail.next = heap[0]
        heap[0] = curr_elem
        heapify(heap, 0, heap_size)
        curr_elem = curr_elem.next
        tail = tail.next
        tail.next = None
    heapify(heap, 0, heap_size)

    while(True):
        tail.next = heap[0]
        
        tail = tail.next
        tail.next = None

        inf_node = Node()
        inf_node.val = float('inf')
        heap[0] = inf_node
        heapify(heap, 0, heap_size)
        if heap[0].val == float('inf'): break
    
    return sentry.next


runtests( SortH ) 
