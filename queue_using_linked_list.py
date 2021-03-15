'''
     Time complexity for both enqueue() and dequeue() is O(1)
'''

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.temp = None 

    def enqueue(self, val):
        node = Node(val)
        if self.rear is None:
            self.rear = node 
            self.temp = node 
        else:
            self.rear.next = node 
            self.rear = node 

    def dequeue(self):
        if self.rear is None:
            print('First enqueue an element!')
        elif self.front is None:
            self.front = self.temp
            print('Dequeued :', self.front.data)    
        elif self.front.next is None:
            print('All element dequeued, no element left!')
        else:
            self.front = self.front.next
            print('Dequeued :', self.front.data)
            

q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(55)
q.enqueue(66)
q.dequeue()
q.dequeue()