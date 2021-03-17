'''
    #### Implementation of Queue using Stack
    Method 2. Enqueue costly:
                    In this approach the time complexity will be:
                    enqueue() --> O(n)
                    dequeue() --> O(1)

    Video to understand the algorithm --> https://www.youtube.com/watch?v=xSa0sD-RqMg&ab_channel=TECHDOSE                
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
        if self.s1.isEmpty():
            self.s1.push(val)
        else:
            while not self.s1.isEmpty():
                element = self.s1.pop()
                self.s2.push(element)
            self.s1.push(val)
            while not self.s2.isEmpty():
                element = self.s2.pop()
                self.s1.push(element)        

    def dequeue(self):
        print(self.s1.pop())


q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()
q.enqueue(8)
q.dequeue()
q.dequeue()
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.dequeue()
q.dequeue()