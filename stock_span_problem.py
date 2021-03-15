'''
    Time complexity: O(n)
    Auxiliary space: O(n)

    Link to understand the concept: https://www.youtube.com/watch?v=-IFmgue8sF0&ab_channel=TECHDOSE
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

    def spanCalc(self, days, price):
        days = days
        span = [1]*days
        price = price
        self.push(0)
        for i in range(1, days):
            while (not self.isEmpty()) and (price[self.peek()] <= price[i]):
                self.pop()
            if self.isEmpty():
                span[i] = i + 1 
            else:
                span[i] = i - self.peek()      
            self.push(i)  
        print(span)        


st = Stack()
price = [10, 4, 5, 90, 120, 80] 
st.spanCalc(len(price), price)