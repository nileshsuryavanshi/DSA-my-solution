class Node:
    count = 0
    def __init__(self, data):
        self.data = data
        self.next = None
        Node.count += 1

class LinkedList:
    def __init__(self):
        self.head = None 

    def delete(self, position):
        # if linked list is empty
        if self.head == None:
            print('Linked list is empty!')
            return 
        # if position is positive and less than the size of linked list    
        elif position < Node.count and position >= 0:
            
            # if the position is 0
            if position == 0:
                temp = self.head
                self.head = temp.next 
                temp = None

            else:
                temp = self.head
                for _ in range(position-1):
                    temp = temp.next 
                temp.next = temp.next.next
        else:
            print('You are giving the position which is out of linked list:)')

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

ll.delete(1)
ll.print_list()