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
        self.top -= 1 
        return popped


    def peek(self):
        # show the top element of stack
        if self.top == -1:
            return None 
        else:
            return self.stack[self.top]        


    def calc(self, s):
        # pop two elements and perform operation on them and push the result into stack
        a = self.pop() 
        b = self.pop()
        if s == '+':
            self.push(a+b) 
        elif s == '-':
            self.push(b-a) 
        elif s == '*':
            self.push(a*b) 
        elif s == '/':
            self.push(b/a)          
        elif s == '^':
            self.push(b**a)      


    def evalPostfix(self, string):
        string = string.split()
        # iterate characters from string
        for s in string:
            # if s is a number then push it directly
            if s.isdigit():
                self.push(int(s))
            # if s is operator then call calc method    
            else:
                self.calc(s) 
        print('Postfix evaluation :',self.peek())                               


# initializing stack object 
st = Stack(40)
st.evalPostfix('100 200 + 2 / 5 * 7 +')
