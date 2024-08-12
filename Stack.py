from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,value):
        self.container.append(value)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def show_stack(self):
        return self.container

a1=Stack()
a1.push(56)
print(a1.show_stack())
print(a1.peek())