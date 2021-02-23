class Stack:
    def __init__(self):
        self.stack = [] 

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print('Stack underflow')
            return 
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack) == 0:
            print('Stack is empty')
        else:
            print('Stack is not empty')

    def peek(self):
        if len(self.stack) == 0:
            return 
        print(self.stack[-1])

    def show(self):
        print(self.stack[::-1]) 

st = Stack()
st.push(5)
st.push(2)
st.push(8)
st.show()
st.pop()
st.show()                                      
st.peek()