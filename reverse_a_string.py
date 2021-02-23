class Stack:
    def __init__(self):
        # stack to store numerical value
        self.stack = [] 


    def isEmpty(self):
        # return True if stack is empty otherwise False
        return True if len(self.stack) == 0 else False  


    def push(self, data):
        # push element into stack
        for d in data:
            self.stack.append(d)


    def pop(self):
        # pop elemnt from stack
        if self.isEmpty():
            return 
        return self.stack.pop()


    def peek(self):
        # return the last element in stack
        if self.isEmpty():
            return 
        return self.stack[-1]

    
    def reverse(self):
        while not self.isEmpty():
            print(self.pop(), end='')
        print()

st = Stack()
st.push('feel you fade')
st.reverse()