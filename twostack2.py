class TwoStack:
    def __init__(self, n):
        self.size = n 
        self.stack = [None]*n  
        self.top1 = -1
        self.top2 = n 

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stack[self.top1] = data 
        else:
            print('Stack1 Overflow')    


    def push2(self, data):
        if self.top2 > self.top1 + 1:
            self.top2 -= 1
            self.stack[self.top2] = data 
        else:
            print('Stack2 Overflow')


    def pop1(self):
        if self.top1 >= 0:
            print('The popped element is :', self.stack[self.top1])
            self.top1 -= 1
        else:
            print('Stack1 Underflow')


    def pop2(self):
            if self.top2 < self.size:
                print('The popped element is :', self.stack[self.top2])
                self.top2 += 1
            else:
                print('Stack2 Underflow')

       
st = TwoStack(8)
st.push1(1)
st.push1(2)
st.push1(3)
st.push1(4)
st.push1(5)
st.push1(6)
st.push2(7)
st.push2(8)
st.pop1()
st.pop1()
st.pop1()
st.pop1()
st.pop1()
st.pop1()
st.pop1()
# st.pop2()
# st.push2(9)
# st.push2(10)