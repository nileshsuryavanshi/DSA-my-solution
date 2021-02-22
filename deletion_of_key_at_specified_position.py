class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def delete(self, position):
        # if linked list is empty
        if self.head == None:
            return
       
        temp = self.head 

        # if position is 0 (first element)
        if position == 0:
            self.head = temp.next 
            temp = None
            return

        for _ in range(position-1):
            temp = temp.next
            if temp == None:
                break  

        # return if the position is more than number of nodes
        if temp is None:
            return 
        if temp.next is None:
            return    

        # unlink the node from the linked list
        next = temp.next.next
        temp.next = None  
        temp.next = next

    def print_list(self):
        temp = self.head 
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print()

ll = LinkedList()
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

ll.head = one 
one.next = two
two.next = three
three.next = four 
ll.print_list()

print('Deleting the 2nd element')
ll.delete(0)
ll.print_list()
