'''
    #Problem:
        Sliding Window Maximum (Maximum of all subarrays of size k)

    Here, I am going to use queue(by linked list) to make sliding window and find 
    maximum of each window.
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
            # print('Dequeued :', self.front.data)    
        elif self.front.next is None:
            # print('All element dequeued, no element left!')
            pass
        else:
            self.front = self.front.next
            # print('Dequeued :', self.front.data)


def window_max(arr, k):
    # making queue object
    q = Queue()
    maximum = arr[0]
    
    # for first k element finding max
    for i in range(k):
        # enqueue first k elements
        q.enqueue(arr[i])
        if maximum < arr[i]:
            maximum = arr[i]

    # printing maximum for first three elements        
    print(maximum)

    # sliding the window
    for i in range(k, len(arr)):
        # dequeue one element and enqueue one element to make window 
        q.enqueue(arr[i])
        q.dequeue()
        if maximum < arr[i]:
            maximum = arr[i]
        print(maximum)                    

array = [1, 2, 3, 1, 4, 5, 2, 3, 6]
window_max(array, 3)               