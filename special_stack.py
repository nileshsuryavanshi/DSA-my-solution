class SpecialStack:
    def __init__(self, n):
        self.size = n
        self.stack = [None]*n
        self.aux = [None]*n
        self.top = -1

    def isEmpty(self):
        print(True if self.top == -1 else False) 

    def push(self, data):
        # push element into stack
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = data

            if self.aux[0] is None:
                self.aux[self.top] = data
            else:
                # if the element we want to push is greater than the previous one then push again the previous one
                if data > self.aux[self.top - 1]:
                    self.aux[self.top] = self.aux[self.top - 1]
                # otherwise push the new element    
                else:
                    self.aux[self.top] = data            
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

    def isFull(self):
        # return true if stack is full otherwise false
        print(True if self.top == self.size - 1 else False) 

    def getMin(self):
        # getting the minimum value of stack
        print(self.aux[self.top])           

st = SpecialStack(5)
st.push(18)
st.getMin()
st.push(19)
st.getMin()        
st.push(29)
st.getMin()
st.push(15)
st.getMin()
st.push(16)
st.getMin()
st.isEmpty()
st.isFull()
st.pop()
st.getMin()
st.pop()
st.getMin()