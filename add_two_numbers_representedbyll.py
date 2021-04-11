'''
### Input:
        List1: 5->6->3 // represents number 365 
        List2: 8->4->2 // represents number 248 

### Output:
        Resultant list: 3->1->6 // represents number 613 
        Explanation: 365 + 248 = 613    
'''

class Node:
    def __init__(self, val):
        self.data = val 
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def summing(self, one, two):
        carry = 0
        lst = []
        while one or two:
            val_1 = one.data if one is not None else 0
            val_2 = two.data if two is not None else 0
            summ = val_1 + val_2 + carry
            if summ > 9:
                val = summ - 10
                carry = 1
            else:
                val = summ 
                carry = 0
            lst.append(str(val))
            if one is None:
                one = None
            else:
                one = one.next 
            if two is None:
                two = None
            else:
                two = two.next
        print(''.join(lst[::-1]))            
        

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print()    

ll = LL()
one = Node(5)
two = Node(6)
three = Node(3)
ll.head = one 
one.next = two 
two.next = three

mm = LL()
a = Node(8)
b = Node(4)
c = Node(2)
mm.head = a
a.next = b
b.next = c

ll.summing(ll.head, mm.head)
