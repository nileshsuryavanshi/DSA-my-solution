class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head is None else False 

    def push(self, data):
        node = Node(data)
        node.next = self.head 
        self.head = node 

    def pop(self):
        if self.isEmpty():
            print('Stack Underflow')
            return 
        temp = self.head 
        self.head = self.head.next 
        popped = temp.data 
        print('The popped element is :', popped)

    def peek(self):
        if self.isEmpty():
            print('Stack Underflow')
            return
        print('The peek element is :', self.head.data)

    def show(self):
        temp = self.head
        if temp is None:
            print('The stack is empty') 
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print()

st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.show()            
st.pop()
st.pop()
st.pop()
st.pop()