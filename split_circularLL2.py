class Node:
    count = 0
    def __init__(self, val):
        self.data = val 
        self.next = None
        Node.count += 1


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

    def split(self, last):
        length = Node.count
        if length%2 != 0:
            ind = int(length/2) + 1
        else:
            ind = int(length/2)
        a = self.head 
        i = 0
        while i < ind - 1:
            a = a.next
            i += 1
        b = a.next
        last.next = b
        a.next = self.head
        return self.head, b 


ll = CLL()
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eigth = Node(8)
ll.head = one
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eigth
eigth.next = one 

ll.traverse()
one = CLL()
two = CLL()
one.head, two.head = ll.split(eigth)
one.traverse()
two.traverse()