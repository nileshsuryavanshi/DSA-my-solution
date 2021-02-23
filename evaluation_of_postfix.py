class Stack:
    def __init__(self):
        # stack to store numerical value
        self.stack = [] 


    def isEmpty(self):
        # return True if stack is empty otherwise False
        return True if len(self.stack) == 0 else False  


    def push(self, data):
        # push element into stack
        self.stack.append(data)


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


    def calculate(self, s):
        if len(self.stack) > 1:
            first = int(self.pop())
            second = int(self.pop())
            if s == '+':
                self.push(second + first)
            elif s == '-':
                self.push(second - first)
            elif s == '*':
                self.push(second * first)
            elif s == '/':
                self.push(second / first)
            elif s == '^':
                self.push(second ** first)
                                

    def evalPostfix(self, string):
        # splitting string into list
        string = string.split()
        for s in string:
            # if the value is digit then push it into stack
            if s.isdigit():
                self.push(s)
            # other wise do the calculation    
            else:
                self.calculate(s)    


st = Stack()
st.evalPostfix('100 200 + 2 / 5 * 7 +')
print(st.peek())
