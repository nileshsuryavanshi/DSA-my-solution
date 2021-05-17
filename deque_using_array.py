'''
    ### Implementation of Deque using array
    ### Time complexity --- O(1) for all operations
'''

class Deque:
    def __init__(self, n):
        self.size = n
        self.queue = [None]*n 
        self.front = self.rear = -1

    def isEmpty(self):
        # return whether queue is empty or not
        return (self.rear == -1) and (self.front == -1)

    def insertFront(self, val):
        # function for inserting element at front
        if (self.front - 1) % self.size == self.rear:
            print('Queue overflow:)')
        else:
            if self.isEmpty():
                self.rear = self.front = 0
            else:
                self.front = (self.front - 1) % self.size       
            self.queue[self.front] = val 

    def insertLast(self, val):
        # function for insering element at last
        if (self.rear + 1) % self.size == self.front:
            print("Queue overflow")
        else:
            if self.isEmpty():
                self.rear = self.front = 0 
            else:
                self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = val 

    def deleteFront(self):
        # function to delete element from front
        if self.isEmpty():
            print('Queue is empty')                
        else:
            if self.front == self.rear:
                print('Dequeued:', self.queue[self.front])
                self.front = self.rear = -1
            else:
                print('Dequeued:', self.queue[self.front])
                self.front = (self.front + 1) % self.size

    def deleteLast(self):
        # function to delete element from last
        if self.isEmpty():
            print('Queue is empty')
        else:
            if self.front == self.rear:
                print('Dequeued:', self.queue[self.rear])
                self.front = self.rear = -1
            else:
                print('Dequeued:', self.queue[self.rear])
                self.rear = (self.rear - 1) % self.size

    def getFront(self):
        # function to show front element
        if self.isEmpty():
            print('Queue is empty')
        else:
            print('Front:', self.queue[self.front])

    def getRear(self):
        # function to show last element
        if self.isEmpty():
            print('Queue is empty')
        else:
            print('Rear:', self.queue[self.rear])

# declaring Deque which contains 5 elements
dq = Deque(5)
dq.insertFront(1)
dq.insertFront(2)
dq.insertFront(3)
dq.insertLast(4)
dq.insertLast(5)
dq.getFront()
dq.getRear()

dq.deleteFront()
dq.deleteLast()
dq.deleteFront()
dq.deleteLast()
dq.deleteLast()