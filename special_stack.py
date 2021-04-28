class Stack:
    def __init__(self, n):
        self.size = n 
        self.stack = [None]*n 
        self.top = -1 
        self.minStack = [None]*n # stack to store minimum values


    def isEmpty(self):
        # return true if stack is empty otherwise false
        return self.top == -1


    def peek(self):
        # show the top element of stack
        if self.top == -1:
            return None 
        else:
            return self.stack[self.top]      


    def isFull(self):
        # return true if stack is full otherwise false
        return self.top == self.size - 1           


    def push(self, val):
        # if top == size-1 then show "stack overflow" else push element in stack 
        if self.top == (self.size - 1):
            print('Stack Overflow')
            return   
        self.top += 1 
        self.stack[self.top] = val 
        # if the element is first element then directly push it into minStack
        if self.top == 0:
            self.minStack[self.top] = val

        # if the peek element of stack is less than the last element in minStack then 
        # push peek element of stack in minStack    
        elif self.peek() < self.minStack[self.top - 1]:
            self.minStack[self.top] = self.peek()

        # otherwise push the last element of minStack into minStack    
        else:
            self.minStack[self.top] = self.minStack[self.top - 1]        


    def pop(self):
        # if top == -1 then show "stack underflow" else pop the element
        if self.top == -1:
            print('Stack Underflow')
            return
        # popped = self.stack[self.top]
        self.top -= 1 
        # return popped 


    def getMin(self):
        # function to get min value present in stack
        print(self.minStack[self.top])        


# initializing stack object 
st = Stack(6)
st.push(10)
st.push(0)
st.push(5)
st.push(2)
st.push(-1)
st.push(98)
st.getMin()
st.pop()
st.pop()
st.getMin()
st.pop()
st.pop()
st.getMin()
st.push(-2)
st.push(52)
st.getMin()
