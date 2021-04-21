'''
   ### Infix to postfix
'''

class Stack:
    def __init__(self, n):
        self.size = n 
        self.stack = [None]*n 
        self.top = -1 
        self.order = {'^':4, '*':3, '%':3, '/':3, '+':2, '-':2, '=':1}


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


    def paren(self, s):
        # if s is "(" then directly push it
        if s == '(':
            self.push(s)   
        # else pop everything until we get "("    
        else:
            while self.peek() != '(':
                popped = self.pop()
                self.stt += popped 
            self.pop()                        


    def operator(self, s):
        # getting the top element
        peek = self.peek()
        # if peek is None or "(" then push s directly
        if peek is None or peek == '(':
            self.push(s)
            return
        if peek == '^' and s == '^':
            self.push(s)  
            return
        # pop operator if the precedence of peek element is higher than s    
        while self.order[peek] >= self.order[s]:
            popped = self.pop()
            self.stt += popped
            peek = self.peek()
            if peek is None or peek == '(':
                break
        self.push(s)  


    def infixToPrefix(self, string):
        self.stt = ''
        # iterate characters from string
        for s in string:
            if s.isalpha():
                self.stt += s 
            elif s == '(' or s == ')':
                self.paren(s)
            elif s in self.order: 
                self.operator(s)  
        
        # pop all the element present in stack and add them to string one by one
        while not self.isEmpty():
            popped = self.pop() 
            self.stt += popped 
        # lastly display the final prefix expression    
        print(self.stt)                    


# initializing stack object 
st = Stack(35)
st.infixToPrefix('a^b^c*d')
