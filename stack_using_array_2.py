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
            print('Stack Overflow')
            return 
        self.top += 1 
        self.stack[self.top] = val 

    def pop(self):
        # if top == -1 then show "stack underflow" else pop the element
        if self.top == -1:
            print('Stack Underflow')
            return
        popped = self.stack[self.top]
        print('The popped element is:', popped)
        self.top -= 1 

    def peek(self):
        # show the top element of stack
        if self.top == -1:
            print('There is no element in stack')
            return
        print(self.stack[self.top])                


st = Stack(5)
st.push(11)
st.push(12)
st.push(13)
st.push(14)
st.push(45)
st.peek()
st.push(88)
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
