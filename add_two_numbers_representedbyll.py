'''
### Input:
        List1: 5->6->3 // represents number 365 
        List2: 8->4->2 // represents number 248 

### Output:
        Resultant list: 3->1->6 // represents number 613 
        Explanation: 365 + 248 = 613    
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        temp = self.head 
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print() 

    def add_ll(self, one, two):
        val_one = 0
        val_two = 0
        carry = 0
        val = 0
        temp = None
        while (one is not None or two is not None):
            if one is not None:
                val_one = one.data  
            else:
                val_one = 0
            if two is not None:
                val_two = two.data 
            else:
                val_two = 0

            val = val_one + val_two + carry
            if val > 9:
                val = val - 10 
                carry = 1
            else:
                val = val 
                carry = 0

            node = Node(val)
            if self.head is None:
                self.head = node  
            else:
                temp.next = node 
            temp = node

            if one is not None:
                one = one.next 
            if two is not None:
                two = two.next    
        if carry > 0:
            temp.next = Node(carry)        
        # return temp         


ll = LinkedList()
one = Node(7)
two = Node(5)
three = Node(9)        
four = Node(4)
five = Node(6)       
ll.head = one 
one.next = two 
two.next = three 
three.next = four
four.next = five

mm = LinkedList()
onem = Node(8)
twom = Node(4)
threem = Node(2)        
fourm = Node(7)       
mm.head = onem 
onem.next = twom 
twom.next = threem 
threem.next = fourm

nn = LinkedList()
nn.add_ll(ll.head, mm.head)
nn.print_ll()
print('end')