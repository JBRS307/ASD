from random import randrange

#Stack
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = Node()
        self.size = 0
    
    def size(self):
        return self.size
    
    def empty(self):
        return self.size == 0
    
    def peek(self):
        if self.empty():
            raise Exception("Peeking from an empty stack")
        
        return self.head.next.val
    
    def push(self, data):
        new_node = Node(data, self.head.next)
        self.head.next = new_node
        self.size += 1
    
    def pop(self):
        if self.empty():
            raise Exception("Popping from an empty stack")
        
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.val
    
    def print(self):
        elem = self.head
        for i in range(self.size):
            elem = elem.next
            print(elem.val, end=" ")
        print()
#End Stack

#Iterative Quicksort
def partition(arr, l, r):
    pivot = arr[r]

    i = l-1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i+1

def iter_quicksort(arr, l, r):
    stack = Stack()
    stack.push(l)
    stack.push(r)

    while not stack.empty():
        r = stack.pop()
        l = stack.pop()
        m = partition(arr, l, r)

        if m-1 > l:
            stack.push(l)
            stack.push(m-1)

        if m+1 < r:
            stack.push(m+1)
            stack.push(r)

if __name__ == "__main__":
    N = 100
    K = 1000

    arr = [randrange(1, K+1) for _ in range(N)]

    print(*arr, end="\n\n")
    iter_quicksort(arr, 0, N-1)
    print(*arr)



