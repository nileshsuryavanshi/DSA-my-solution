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
        self.front = -1
        self.rear = -1
        self.queue = [None]*n 
        self.size = n 

    def enqueue(self, data):
        # enqueue upto the size of queue
        if self.rear < self.size - 1:
            self.rear += 1
            self.queue[self.rear] = data
        # when queue is full show overflow message       
        else:
            print('Queue overflow')

    def dequeue(self):
        # if the front is less than rear only then perform dequeue
        if self.front < self.rear:
            print('Dequeued element is :', self.queue[self.front + 1])
            self.front += 1
        elif self.rear == -1:
            # if queue is empty then show message to perform enqueue
            print('Please enqueue an element!')
        else:
            print('Queue underflow')

    def frontt(self):
        # function returns the front element of the queue
        if self.front == -1:
            print('No element is there in queue!')
        else:
            print('The front element is :', self.queue[self.front + 1])

    def rearr(self):
        # function returns the rear element of the queue
        if self.rear == -1:
            print('No element is there in queue!') 
        else:
            print('The rear element is :', self.queue[self.rear])  

q = Queue(5)
q.enqueue(1)
q.enqueue(2)                                                         
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.dequeue()
q.frontt()
q.rearr()