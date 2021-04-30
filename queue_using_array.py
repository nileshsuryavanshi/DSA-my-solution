'''
    ## Time Complexity: 
        Operations              Complexity
        Enque(insertion)           O(1)
        Deque(deletion)            O(1)
        Front(Get front)           O(1)
        Rear(Get Rear)             O(1)              

    ## Auxiliary Space: O(N). 
        N is the size of array for storing elements.
'''

class Queue:
    def __init__(self, n):
        self.size = n 
        self.queue = [None]*n
        self.front = self.rear = -1 


    def enqueue(self, val):
        # if rear == size-1 then show queue overflow
        if self.rear == self.size-1:
            print('Queue overflow')
        # if rear < size-1 then increase rear    
        elif self.rear < self.size-1:
            if self.rear == -1 and self.front == -1:
                self.rear = self.front = 0 
            else:
                self.rear += 1
            self.queue[self.rear] = val           


    def dequeue(self):
        # if front = -1 the show that queue is empty
        if self.front == -1:
            print('Queue is empty') 
        # else increase front     
        else:
            if self.rear == self.front:
                print('Dequeued:', self.queue[self.front])
                self.front = self.rear = -1 
            else:
                print('Dequeued:', self.queue[self.front]) 
                self.front += 1 


    def getFront(self):
        # if front = -1 then show queue is empty
        if self.front == -1:
            print('Queue is empty')
        # otherwise show element present at front    
        else:    
            print('Element present at front:', self.queue[self.front])

    def getRear(self):
        # if rear = -1 then show queue is empty
        if self.rear == -1:
            print('Queue is empty')
        # otherwise show element present at rear    
        else:    
            print('Element present at rear:', self.queue[self.rear])    


# making queue of size 5 to store only 5 elements
q = Queue(5)
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)
q.enqueue(55)
q.getFront()
q.getRear()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.getRear()