'''
    #Problem:
        Print the binary of first n numbers

    By using queue the time complexity will be O(n).
    This approach is taken from GeeksForGeeks.    
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
            # print('First enqueue an element!')
            pass
        elif self.front is None:
            self.front = self.temp
            return self.front.data  
        elif self.front.next is None:
            # print('All element dequeued, no element left!')
            pass
        else:
            self.front = self.front.next
            return self.front.data


def nbinary(n):
    # making queue object
    q = Queue()
    q.enqueue('1')
    while n>0:
        n -= 1
        one = q.dequeue()
        print(one)
        two = one 
        q.enqueue(str(one)+'0')
        q.enqueue(str(two)+'1')

nbinary(10)               