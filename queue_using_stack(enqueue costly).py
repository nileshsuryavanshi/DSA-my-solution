'''
    #### Implementation of Queue using Stack
    Method 2. Enqueue costly:
                    In this approach the time complexity will be:
                    enqueue() --> O(n)
                    dequeue() --> O(1)

    Video to understand the algorithm --> https://www.youtube.com/watch?v=xSa0sD-RqMg&ab_channel=TECHDOSE                
'''

class Stack:
    def __init__(self, n):
        self.size = n 
        self.stack = [None]*n 
        self.top = -1 

    def isEmpty(self):
        # return true if stack is empty otherwise false
        return self.top == -1

    def push(self, val):
        # if top == size-1 then show "stack overflow" else push element in stack 
        if self.top == (self.size - 1):
            print('Queue Overflow')
            return 
        self.top += 1 
        self.stack[self.top] = val 

    def pop(self):
        # if top == -1 then show "stack underflow" else pop the element
        if self.top == -1:
            print('Stack Underflow')
            return
        popped = self.stack[self.top]
        self.top -= 1 
        return popped

class Queue:
    def __init__(self, n):
        # initialize two stacks
        self.s1 = Stack(n)
        self.s2 = Stack(n)

    def enqueue(self, val):
        # if s1 is empty then directly push the element into it
        if self.s1.isEmpty():
            self.s1.push(val)
        # else pop all elements from s1 and push them into s2
        # then push the current element into s1 now pop all 
        # the elements from s2 and push them back into s1    
        else:
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
            self.s1.push(val)
            while not self.s2.isEmpty():
                self.s1.push(self.s2.pop())    

    def dequeue(self):
        # if s1 not empty then dequeue otherwise show 'Queue is empty' message
        if not self.s1.isEmpty():
            print('Dequeued:', self.s1.pop())
        else:
            print('Queue is empty')


q = Queue(5)
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()