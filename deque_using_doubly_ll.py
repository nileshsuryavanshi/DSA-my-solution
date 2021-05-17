'''
    ### Implementation of Deque using Doubly Linked List
    ### Time complexity --- O(1) for all operations
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None


class Deque:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        # returns whether queue is empty or not
        return (self.front is None) and (self.rear is None)

    def insertFront(self, val):
        # function for inserting element at front
        node = Node(val)
        if self.isEmpty():
            self.front = self.rear = node 
        else:
            self.front.prev = node 
            node.next = self.front
            self.front = node     

    def insertLast(self, val):
        # function for insering element at last
        node = Node(val)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node 
            node.prev = self.rear 
            self.rear = node 

    def deleteFront(self):
        # function to delete element from front
        if self.isEmpty():
            print('Queue is empty')
        else:
            if self.rear == self.front:
                print('Dequeued:', self.front.data)
                self.front = self.rear = None
            else:    
                print('Dequeued:', self.front.data)
                self.front = self.front.next
                self.front.prev = None

    def deleteLast(self):
        # function to delete element from last
        if self.isEmpty():
            print('Queue is empty')
        else:
            if self.rear == self.front:
                print('Dequeued:', self.rear.data)
                self.front = self.rear = None
            else:
                print('Dequeued:', self.rear.data)
                self.rear = self.rear.prev
                self.rear.next = None

    def getFront(self):
        # function to show front element
        if self.isEmpty():
            print('Queue is empty')
        else:
            print('Front:', self.front.data)

    def getRear(self):
        # function to show last element
        if self.isEmpty():
            print('Queue is empty')
        else:
            print('Rear:', self.rear.data)
        

dq = Deque()
# inserting elements
dq.insertFront(1)
dq.insertFront(2)
dq.insertFront(3)
dq.insertLast(4)
dq.insertLast(5)
dq.getFront()
dq.getRear()

# deleting elements
dq.deleteFront()
dq.deleteLast()
dq.deleteFront()
dq.deleteLast()
dq.deleteLast()
dq.deleteFront()