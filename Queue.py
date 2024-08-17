from collections import deque
class Queue:
    def __init__(self):
        self.storage=deque()
    def inqueue(self,value):
        self.storage.appendleft(value)
    def outqueue(self):
        return self.storage.pop()
    def size(self):
        return len(self.storage)
    def is_empty(self):
        return len(self.storage)==0
    def show_queue(self):
        return self.storage

q1=Queue()
q1.inqueue(23)
print(q1.show_queue())
