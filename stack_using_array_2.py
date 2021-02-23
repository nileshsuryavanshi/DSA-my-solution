class Stack:
    def __init__(self, n):
        # stack to store numerical value
        self.size = n 
        self.stack = [None]*n  
        self.top = -1


    def isEmpty(self):
        # return True if stack is empty otherwise False
        result = True if self.top == -1 else False
        print(result)  


    def push(self, data):
        # push element into stack
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = data 
        else:
            print('Stack Overflow')


    def pop(self):
        # pop elemnt from stack
        if self.top >= 0:
            print('The popped element is :', self.stack[self.top])
            self.top -= 1
        else:
            print('Stack Underflow')


    def peek(self):
        # return the last element in stack
        if self.top == -1:
            print(None)
        else:    
            print(self.stack[self.top])
       

st = Stack(5)
st.isEmpty()
st.push(11)
st.push(12)
st.push(13)
st.push(14)
st.peek()
st.isEmpty()
st.push(45)
st.peek()
st.push(88)