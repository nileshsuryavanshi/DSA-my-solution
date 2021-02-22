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

def merge_sl(a, b):
    dummy = Node(0)
    tail = dummy

    while True:
        if a is None:
            tail.next = b
            break 
        elif b is None:
            tail.next = a 
            break 
        if a.data < b.data:
            tail.next = a 
            a = a.next 
        else:
            tail.next = b 
            b = b.next 
        tail = tail.next
    return dummy.next                 


first_ll = LinkedList()
aa = Node(2)
bb = Node(8)
cc = Node(15)
dd = Node(16)
first_ll.head = aa
aa.next = bb
bb.next = cc 
cc.next = dd 

second_ll = LinkedList()
ee = Node(1)
ff = Node(3)
gg = Node(3)
hh = Node(7)
# ii = Node(10)
second_ll.head = ee 
ee.next = ff 
ff.next = gg 
gg.next = hh 
# hh.next = ii 

first_ll.head = merge_sl(first_ll.head, second_ll.head)
first_ll.print_ll()