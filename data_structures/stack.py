from random import randrange

#Stack
class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None

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
            print("Stack is empty")
            return
        
        return self.head.next.val

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1
    
    def pop(self):
        if self.empty():
            print("Stack is empty")
            return
        
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.val
    
    def print(self):
        elem = self.head.next
        for _ in range(self.size):
            print(elem.val, end=" ")
            elem = elem.next
        print()
#End Stack

if __name__ == "__main__":
    N = 10
    K = 100

    stack = Stack()

    for _ in range(N):
        stack.push(randrange(1, K+1))
    stack.print()
    print(stack.peek())

    print()
    for _ in range(N//2):
        stack.pop()
    stack.print()
    print(stack.peek())
