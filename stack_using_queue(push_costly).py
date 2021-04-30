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
            popped = self.front.data
            self.front = self.front.next 
            if self.front is None:
                self.rear = None 
            return popped    

    def isEmpty(self):
        return self.front is None 


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        if self.q1.isEmpty():
            self.q1.enqueue(val)
        else:
            self.q2.enqueue(val)
            while not self.q1.isEmpty():
                self.q2.enqueue(self.q1.dequeue())      
            self.temp = self.q1
            self.q1 = self.q2
            self.q2 = self.temp

    def pop(self):
        if not self.q1.isEmpty():
            print('Popped:', self.q1.dequeue())
        else:
            print('Stack underflow')   


st = Stack()
st.push(11)
st.push(22)                                                   
st.push(33)
st.push(44)
st.push(55)
st.push(100)
st.pop()
st.pop()
st.pop()
st.pop()