class Node:
    '''
       creating a class to mimic node, which contains
       data and pointer to next node
       ____________        ____________
       |value|next|------->|value|next|
       ------------        ------------
    '''
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    '''
       This class will initiate a linked list by considering
       a head with default value as None
    '''
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


### making a linked list object without taking user's input -------------------------
ll = LinkedList()

### making nodes
one = Node(1)
second = Node(2)
third = Node(3)

### connecting nodes
ll.head = one             # head pointing to first node
one.next =  second        # first node pointing to second node
second.next = third       # second node pointing to third node

### printing the linked list elements
ll.print_list()                      
############################################# ---------------------------------------

  

  
###### make linked list by taking users input ---------------------------------------
# ll = LinkedList()

# take = int(input('Enter the number of node you need : '))

# for i in range(take):
#     val = int(input('Enter value for node : '))
#     node = Node(val)
#     if i == 0:
#         ll.head = node 
#     else:
#         temp.next = node 
#     temp = node          

# ll.print_ll()
############################################# ----------------------------------------