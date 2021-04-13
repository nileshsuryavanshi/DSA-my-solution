'''
Program to perform deletion in doubly linked list.
'''

# importing module for garbage collection
import gc

class Node:
    count = 0
    def __init__(self, data):
        # making two pointers prev and next
        self.data = data 
        self.next = None
        self.prev = None 
        Node.count += 1


class DLL:
    def __init__(self):
        # head to locate first node
        # tail to locate last node
        self.head = None 
        self.tail = None

    def push(self, val):
        node = Node(val)
        # if head is node i.e., linked list is empty
        # then point head and tail to the node
        if self.head is None:
            self.head = node 
            self.tail = node

        # else link the node to tail    
        else:
            self.tail.next = node 
            node.prev = self.tail 
            self.tail = node

    def traverse(self):
        # function to display element present in linked list
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print() 

    def deleteFirst(self):
        self.head = self.head.next 
        self.head.prev = None 
        Node.count -= 1
        gc.collect()

    def deleteLast(self):
        self.tail = self.tail.prev 
        self.tail.next = None
        Node.count -= 1 
        gc.collect()

    def deleteAt(self, pos):
        # if position is positive and less than size of linked list
        if pos < Node.count and pos >= 0:
            # if position is 0 then call deleteFirst() method and return
            if pos == 0:
                self.deleteFirst()
                return
            # if position if count-1 then call deleteLast() method and return
            if pos == Node.count - 1:
                self.deleteLast()
                return
            temp = self.head 
            i = 0
            while i < pos - 1:
                temp = temp.next 
                i += 1
            previous = temp 
            temp.next = temp.next.next
            temp.prev = previous
            Node.count -= 1
            gc.collect()
        # if position doesn't fulfill the above criteria then show message given below
        else:
            print('The position is either more than size of linked list or negative!')            


'''
   Note: Make sure you call the deletion methods after inserting elements in linked list.
'''

# making DLL object and pushin elements
ll = DLL() 
ll.push(1)

ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.traverse()

# deleting first node
ll.deleteFirst()
ll.traverse()

# deleting last node
ll.deleteLast()
ll.traverse()

# deleting node present at specified index
ll.deleteAt(1)
ll.traverse()           