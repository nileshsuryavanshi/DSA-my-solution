'''
    #### Implementation of Queue using Stack
    Method 1. Dequeue costly:
                    In this approach the time complexity will be:
                    enqueue() --> O(1)
                    dequeue() --> O(n)
'''

class Stack:
    def __init__(self):
        self.stack = [] 

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return 
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, val):
        self.s1.push(val)

    def dequeue(self):
        while not self.s1.isEmpty():
            element = self.s1.pop()
            self.s2.push(element)
        print(self.s2.pop())
        while not self.s2.isEmpty():
            element = self.s2.pop()
            self.s1.push(element)


q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.dequeue()
q.dequeue()