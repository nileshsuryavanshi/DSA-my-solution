class Stack:
    def __init__(self, n):
        # stack to store numerical value
        self.size = n 
        self.stack = [None]*n  
        self.top = -1


    def isEmpty(self):
        # return True if stack is empty otherwise False
        return True if self.top == -1 else False 


    def push(self, data):
        # push element into stack
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = data 
        else:
            print('Stack Overflow')


    def pop(self):
        # pop elemnt from stack
        if self.top >= 0:
            self.top -= 1
        else:
            print('Stack Underflow')


    def peek(self):
        # return the last element in stack
        if self.top == -1:
            return 
        else:    
            return self.stack[self.top]

    def nge(self, arr):
        # pushing first element of array
        self.push(arr[0])
        # iterate from second element to the last element of array
        for i in range(1, len(arr)):
            if self.peek() < arr[i]:
                print(self.peek(), '--->', arr[i])
                self.pop()
                while (not self.isEmpty()) and (self.peek() < arr[i]):
                    popped = self.peek()
                    self.pop()
                    print(popped, '--->', arr[i])
                self.push(arr[i])    
            else:
                self.push(arr[i])
        while not self.isEmpty():
            top_element = self.peek()
            self.pop()
            print(top_element, '---> -1')   


arr = [1, 5, 7, 0, 52, 30]
st = Stack(len(arr))
st.nge(arr)