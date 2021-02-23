'''
   ### Infix to postfix
'''

class Stack:
    def __init__(self):
        # stack to store operators only
        self.stack = [] 
        # list to store output
        self.output = [] 
        self.operators = {'^':3, '*':2, '/':2, '+':1, '-':1}


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


    def isOperator(self, s):
        # taking the top element from stack
        top = self.peek()
        if self.isEmpty() or top == "(":
            self.push(s)
        else:
            '''
               compare if the precedence of current element(s) is less than top element from the stack
               if it is less than pop the top element from the stack and check again until the precedence
               of top < s.
            ''' 
            while self.operators[s] <= self.operators[top]:
                popped = self.pop()
                self.output.append(popped)
                if not self.isEmpty():
                    top = self.peek()
                    # break the loop if top element is open paranthesis
                    if top == "(":
                        break 
                else:
                    break    
            # push the element s     
            self.push(s) 


    def parenCheck(self, s):
        if s == "(":
            self.push(s)
        else:
            popped = self.pop()
            while popped != "(":
                # push until we get open paranthesis
                self.output.append(popped)
                popped = self.pop()  


    def toPostfix(self, string):
        for s in string:
            if s.isalpha():
                # if the element of string is alphabet then directly append it to output list
                self.output.append(s)
            elif s in self.operators:
                # if it is an operator then call the isOperator() method
                self.isOperator(s)
            elif (s == "(" or s == ")"):
                # if it is parenthesis then call parenCheck() method
                self.parenCheck(s)             

        while not self.isEmpty():
            # add element to output list until the stack get empty
            popped = self.pop()
            self.output.append(popped)


st = Stack()
st.toPostfix("a*(b+c*d)+e")
print(''.join(st.output))