'''
    ### Design a stack with operations on middle element

    ### Time complexity: 
        Time complexity for each operation is O(1)
'''
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.mid = None  # will point to mid node
        self.count = 0  

    def push(self, val):
        node = Node(val)
        # if head is none then assign the node to head
        if self.head is None:
            self.head = node
            self.mid = node  
        # otherwise point next of new node to head and assign head the new node    
        else:
            node.next = self.head 
            self.head.prev = node
            self.head = node
            # change mid node only when the count variable is even
            if self.count % 2 == 0:
                self.mid = self.mid.prev
        # increase the value of count variable by 1 with each push operation        
        self.count += 1              

    def pop(self):
        # if head is none i.e., stack is empty then show "Stack Underflow"
        if self.head is None:
            print('Stack Underflow')
        # else pop the element and point head to the next node    
        else:
            popped = self.head.data 
            print('Popped:', popped)
            self.head = self.head.next
            if self.head is not None: 
                self.head.prev = None
            # decrease the value of count variable by 1 with each pop operation    
            self.count -= 1
            # when count becomes 0 then assign none to mid and return
            if self.count == 0:
                self.mid = None
                return
            # if count is even number then assign mid the next node    
            if self.count % 2 == 0:
                self.mid = self.mid.next    

    def isEmpty(self):
        print(self.head is None) 

    def findMiddle(self):
        # function to show mid element of stack
        if self.count == 0:
            print(None)
        elif self.count % 2 == 0 and self.count != 2:
            print(self.mid.prev.data)
        else:
            print(self.mid.data) 

    def deleteMiddle(self):
        # function to delete the mid element of stack
        if self.count == 1:
            self.head = self.mid = None
            self.count -= 1
            return 
        if self.count == 2:
            self.mid = self.mid.prev 
            self.mid.next = None
            self.count -= 1 
            return 
        if self.count % 2 == 0:
            self.mid = self.mid.prev 
        self.count -= 1
        self.mid.prev.next = self.mid.next 
        self.mid.next.prev = self.mid.prev 
        self.mid = self.mid.next                            


st = Stack()
st.push(11)
st.push(22)
st.push(33)
st.push(44)
st.push(55)
st.push(66)
st.push(77)
st.pop()
st.pop()
st.findMiddle()