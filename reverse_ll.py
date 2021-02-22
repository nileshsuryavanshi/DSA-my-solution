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

    def reverse(self):
        prev = None 
        cur = self.head 
        nest = None 

        while cur:
            nest = cur.next 
            cur.next = prev 
            prev = cur 
            cur = nest 
        self.head = prev       

# creating linked list object
ll = LinkedList()
print('Put the values for linked list : ')
take = list(map(int, input().split()))

# making and linking nodes
for i, val in enumerate(take):
    node = Node(val)
    if i == 0:
        ll.head = node 
    else:
        temp.next = node 
    temp = node          

ll.reverse()
ll.print_ll()