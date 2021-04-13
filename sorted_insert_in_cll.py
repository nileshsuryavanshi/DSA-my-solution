'''
   ### Problem statement:
       Write a program to insert a new node in a sorted circular linked list.
   
   ### Time Complexity : O(n)
'''

class Node:
    def __init__(self, val):
        self.data = val 
        self.next = None


class CLL:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        tid = id(temp) 
        while True:
            if id(temp.next) == tid:
                print(temp.data)
                break 
            print(temp.data, end=' ')  
            temp = temp.next    

    def sorted_insert(self, val):
        prev = self.head
        temp = prev.next
        node = Node(val)
        pid = id(prev)
        flag = 0
        while not id(temp) == pid:
            # if node data is between prev and temp data
            if prev.data <= node.data <= temp.data:
                node.next = temp
                prev.next = node
                flag = 1
                break 
            prev = temp 
            temp = temp.next

        # if node data is smallest or bigest of all    
        if flag == 0:
            node.next = temp
            prev.next = node
            # if node data is smallest of all 
            # point head to it
            if node.data <= temp.data:
                self.head = node 



ll = CLL()
one = Node(1)
two = Node(3)
three = Node(8)
four = Node(10)
five = Node(13)
six = Node(18)
seven = Node(25)
eigth = Node(29)
ll.head = one
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eigth
# making CLL(connecting last node to head nead)
eigth.next = one 

print('Before insertion:')
ll.traverse()
ll.sorted_insert(23)
ll.sorted_insert(-22)
print('After insertion:')
ll.traverse()
