'''
   Time complexity: O(n^2)
   Auxiliary space: O(n)
'''

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

    def arrange(self, temp):
        # function to arrange elements in descending order
        if self.isEmpty() or self.peek() < temp:
            self.push(temp)
            return

        element = self.pop()
        self.arrange(temp)
        self.push(element)      

    def sort(self):
        if self.isEmpty():
            return
        else:
            # pop each element from stack
            temp = self.pop()
            self.sort()
            # arranging them in order(ascending or descending)
            self.arrange(temp)    
            

st = Stack()
st.push(120)
st.push(0)
st.push(14)
st.push(21)
st.push(-2)
st.sort()
print(st.stack)