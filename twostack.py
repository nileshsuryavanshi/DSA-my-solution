from math import floor
class TwoStack:
    def __init__(self, n):
        # stack to store numerical value
        self.size = n 
        self.stack = [None]*n  
        self.top1 = -1
        self.top2 = floor(n/2)

    def push1(self, data):
        if self.top1 < floor(self.size/2) - 1:
            self.top1 += 1
            self.stack[self.top1] = data 
        else:
            print('Stack1 Overflow')    

    def push2(self, data):
        # push element into stack
        if self.top2 <= self.size-1:
            # self.top2 += 1
            self.stack[self.top2] = data 
            self.top2 += 1
        else:
            print('Stack2 Overflow')


    def pop1(self):
        # pop elemnt from stack
        if self.top1 >= 0:
            print('The popped element is :', self.stack[self.top1])
            self.top1 -= 1
        else:
            print('Stack1 Underflow')


    def pop2(self):
            # pop elemnt from stack
            if self.top2 > floor(self.size/2):
                self.top2 -= 1
                print('The popped element is :', self.stack[self.top2])
                # self.top2 -= 1
            else:
                print('Stack2 Underflow')

       
st = TwoStack(7)
st.push1(1)
st.push1(2)
st.push1(3)
st.push1(3.5)
st.pop1()
st.pop1()
st.pop1()
st.pop1()
st.push2(4)
st.push2(5)
st.push2(6)
st.push2(7)
st.pop2()
st.pop2()
st.pop2()
st.pop2()
# st.pop2()