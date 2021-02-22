import math 
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class Circular_list:
    def __init__(self):
        self.last = None 
        self.count = 0

    def push(self, val):
        self.count += 1
        if self.last == None:
            self.last = Node(val)
            self.last.next = self.last 
            return
        node = Node(val)
        node.next = self.last.next
        self.last.next = node 

    def splitCl(self):
        temp = self.last.next
        slow = temp
        fast = temp.next 
        while True:
            slow = slow.next 
            fast = fast.next.next
            if fast.next == temp:
                fast.next = slow.next 
                slow.next = temp 
                break 
            if fast.next.next == temp:
                fast = fast.next 
                fast.next = slow.next.next 
                slow = slow.next 
                slow.next = temp
                break 
        return fast, slow     

    def traverse(self):
        if self.last == None:
            print('The linked list is empty')
            return
        temp = self.last.next  
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
            if temp == self.last.next:
                break 
        print() 


cl = Circular_list()
cl.push(1)
cl.push(2)
cl.push(3)
cl.push(4)
cl.push(5)
cl.push(6)
cl.push(8)
cl.traverse()
fast = Circular_list()
slow = Circular_list()
fast.last , slow.last = cl.splitCl()
print('After spliting the cicular linked list:')
slow.traverse()
fast.traverse()
