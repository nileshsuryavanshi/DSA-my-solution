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


    def func(self, s):
        # if stack is not empty then check if top bracket is open 
        if not self.isEmpty():
            a = self.peek()
            if s == ']' and a == '[':
                self.pop()
            elif s == ')' and a == '(':
                self.pop()
            elif s == '}' and a == '{':
                self.pop() 
            else:
                return
        # if the first bracket is closed then show error and halt the program        
        else:
            print('Not balanced:)')
            exit(0)                


    def balanceBracks(self, string):
        # iterate given string
        for s in string:
            # if bracket is open then push it
            if s == '(' or s == '{' or s == '[':
                self.push(s)
            # else call the func() function    
            elif s == ')' or s == '}' or s == ']':
                self.func(s)      
            # if string is anything except brackets then move to next iteration    
            else:
                continue                                  
        # if the stack is empty then show expression is balanaced else not    
        if self.isEmpty():
            print('Balanced')
        else:
            print('Not Balanced')            


# initializing stack object 
st = Stack(40)
st.balanceBracks('([{[{{[]}()}]}])')