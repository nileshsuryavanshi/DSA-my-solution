class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, val):
        node = Node(val)
        if self.rear is None:
            self.rear = self.front = node             
        else:
            self.rear.next = node 
            self.rear = node 

    def dequeue(self):
        if self.front is None:
            print('Queue is empty')
        else:
            print('Dequeued:', self.front.data)
            self.front = self.front.next 
            if self.front is None:
                self.rear = None

    def getFront(self):
        if self.front is None:
            print('Queue is empty')
        else:
            print('Front element:', self.front.data)

    def getRear(self):
        if self.rear is None:
            print('Queue is empty')
        else:
            print('Rear element:', self.rear.data)


q = Queue()
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)
q.enqueue(55)
q.dequeue()
q.dequeue()
q.dequeue()
q.getFront()
q.getRear()                       
