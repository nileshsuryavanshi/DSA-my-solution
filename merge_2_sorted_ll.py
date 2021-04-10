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

    def merge(self, c1, c2):
        # making a dummy node
        dummy = Node(0)
        temp = dummy
        while c1 or c2:
            # if c2 data is less than equal to c1 data then
            # linked dummy node with c2
            if c2.data <= c1.data:
                dummy.next = c2
                dummy = c2
                # if next element of c2 is null
                # then connect link to c1
                if c2.next is None:
                    dummy.next = c1
                    break
                else:
                    c2 = c2.next 
            else:
                dummy.next = c1 
                dummy = c1 
                # if next element of c1 is null
                # then connect link to c2
                if c1.next is None:
                    dummy.next = c2
                    break 
                else:
                    c1 = c1.next 
        # return the second node of dummy ll            
        return temp.next                    


first_ll = LinkedList()
aa = Node(2)
bb = Node(3)
cc = Node(20)
dd = Node(24)
first_ll.head = aa
aa.next = bb
bb.next = cc 
cc.next = dd 

second_ll = LinkedList()
ee = Node(5)
ff = Node(10)
gg = Node(20)
hh = Node(22)
ii = Node(30)
second_ll.head = ee 
ee.next = ff 
ff.next = gg 
gg.next = hh 
hh.next = ii 

# passing head of both linked list to merge method
first_ll.head = first_ll.merge(first_ll.head, second_ll.head)
first_ll.print_ll()