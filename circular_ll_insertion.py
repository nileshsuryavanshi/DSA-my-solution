'''
   Insertion of node at beginning, ending and at any point in circular linked list.
'''

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class Circular_list:
    def __init__(self):
        self.last = None 

    def addToEmpty(self, val):
        if self.last != None:
            return self.last 

        temp = Node(val)
        self.last = temp 

        self.last.next = self.last 
        return self.last 

    def addAtFirst(self, val):
        if self.last == None:
            self.addToEmpty(val)

        node = Node(val)
        node.next = self.last.next 
        self.last.next = node  

    def addAtLast(self, val):
        if self.last == None:
            self.addToEmpty(val)

        node = Node(val)
        node.next = self.last.next 
        self.last.next = node 
        self.last = node 

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

    def atAnyPlace(self, position, val):
        node = Node(val)
        if position == 0:
            self.addAtFirst(val)
            return
        temp = self.last.next
        for _ in range(position-1):
            temp = temp.next 
        node.next = temp.next 
        temp.next = node     


cl = Circular_list()
cl.addToEmpty(5)
cl.addAtFirst(1)
cl.addAtLast(10)
cl.addAtLast(11)
cl.addAtFirst(586)
cl.addAtLast(12)
cl.addAtLast(10)
cl.addAtLast(13)
cl.traverse()
cl.atAnyPlace(4, 66)
cl.traverse()