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
            print('There is no element in stack')
            return
        print(self.stack[self.top])        

    def reverse(self, string):
        # first push each character from string to 
        # stack one by one
        for i in string:
            self.push(i) 

        # then pop each character one by one from stack
        for i in string:
            print(self.pop(), end='')       
        print()             


# initializing stack of size 20
st = Stack(20)
st.reverse('abcdef ghijkl')