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

    def frontInsert(self, val):
        # if linked list is empty then call push option
        if self.head is None:
            self.push(val)
            return
        node = Node(val)
        node.next = self.head 
        self.head.prev = node 
        self.head = node 

    def endInsert(self, val):
        # if linked list is empty then call push option
        if self.head is None:
            self.push(val)
            return
        node = Node(val)
        node.prev = self.tail
        self.tail.next = node 
        self.tail = node 

    def insertAt(self, pos, val):
        # insert element only if the position is positive
        # and less than the size of linked list
        if pos < Node.count and pos >= 0:
            # if position is 0 then call the frontInsert() method and return
            if pos == 0:
                self.frontInsert(val)
                return    
            temp = self.head 
            i = 0
            node = Node(val)
            while i < pos:
                previous = temp 
                temp = temp.next 
                i += 1
            node.next = previous.next 
            node.prev = temp.prev 
            previous.next = node 
            temp.prev = node   

        # display message if the position doesn't fulfill above criteria      
        else:
            print('The position is greater than size of linked list or negative!')    


# making DLL object
ll = DLL() 
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.traverse()

# inserting 5 at front
ll.frontInsert(5)

# inserting 6 at end
ll.endInsert(6)

# displaying updated linked list
ll.traverse()

# inserting 12 at 5th index
ll.insertAt(2, 12)

# displaying updated linked list
ll.traverse()