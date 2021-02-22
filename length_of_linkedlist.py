class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def length(self):
        temp = self.head

        # if head is none then length of linked list is 0
        if temp == None:
            print('The length of linked list is :',0)
            return
        
        # iterate until temp reaches last node
        i = 0
        while temp:
            temp = temp.next
            i += 1
        print('The length of linked list is :', i)            


### making a linked list object
ll = LinkedList()

### making nodes
one = Node(1)
second = Node(2)
third = Node(3)

### connecting nodes
ll.head = one             
one.next =  second        
second.next = third       

### printing the linked list elements
ll.print_list()   
ll.length()                   