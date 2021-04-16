class Node:
    # node to store data and reference to next node
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Stack:
    def __init__(self):
        # initialising head which will work as top
        self.head = None

    def isEmpty(self):
        # if head is none then true otherwise false
        return self.head is None

    def push(self, val):
        # pushing new node and updating top(head)
        node = Node(val)
        node.next = self.head
        self.head = node

    def pop(self):
        # if stack is empty then show message "Stack Underflow"
        if self.isEmpty():
            print('Stack Underflow')
            return 
        # otherwise remove node and update top(head)
        print('The popped element is:', self.head.data)     
        self.head = self.head.next

    def peek(self):
        # if stack is empty then show message given below
        if self.isEmpty():
            print('There is no element in stack')
            return 
        # otherwise show top(head) element    
        print(self.head.data)      


st = Stack()
print(st.isEmpty())
st.push(1)
print(st.isEmpty())
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.pop()
st.pop()
st.pop()
st.pop()
print(st.isEmpty())
st.pop()
print(st.isEmpty())
st.pop()
print(st.isEmpty())
