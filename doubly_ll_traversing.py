class Node:
    def __init__(self, data):
        # making two pointers prev and next
        self.data = data 
        self.next = None
        self.prev = None 


class DLL:
    def __init__(self):
        # head to locate first node
        # tail to locate last node
        self.head = None 
        self.tail = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print() 

    def rev_traverse(self):
        temp = self.tail 
        while temp:
            print(temp.data, end=' ')
            temp = temp.prev 
        print()


# making DLL object
ll = DLL()

take = int(input('Enter the number of node you want in linked list:\n'))
for i in range(take):
    node = Node(int(input()))
    if i == 0:
        ll.head = node 
        temp = node 
    else:
        temp.next = node 
        node.prev = temp
        temp = node 
ll.tail = temp  

# traversing 
ll.traverse()

# reverse traversing
ll.rev_traverse()           