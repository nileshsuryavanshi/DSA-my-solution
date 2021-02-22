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

    def reverse(self, head, k):
        if head == None:
            return None 
        prev = None 
        cur = head 
        nest = None 
        count = 0
        while (cur is not None and count < k):
            nest = cur.next 
            cur.next = prev 
            prev = cur
            cur = nest 
            count += 1
        if nest is not None:
            head.next = self.reverse(nest, k)
        return prev    

ll = LinkedList()
take = int(input('Enter the number of node you need : '))

for i in range(take):
    val = int(input('Enter value for node : '))
    node = Node(val)
    if i == 0:
        ll.head = node 
    else:
        temp.next = node 
    temp = node          

ll.print_ll()
ll.head = ll.reverse(ll.head, 3)
ll.print_ll()