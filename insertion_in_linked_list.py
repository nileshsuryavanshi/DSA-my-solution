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
            print(temp.data, end= ' ')
            temp = temp.next
        print()

    def at_starting(self, new_data):
        new_node = Node(new_data) 
        new_node.next = self.head
        self.head = new_node

    def at_any_place(self, prev_node, new_data):
        if prev_node is None:
            print('The given previous node must be in linked list')
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def at_ending(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 

        last = self.head
        while last.next:
            last = last.next 

        last.next = new_node 
                    
ll = LinkedList()
first = Node(11)
second = Node(22)
third = Node(33)

ll.head = first
first.next = second
second.next = third

print('Before insertion, the linked list is :')
ll.print_list()

### inserting at the starting of linked list
ll.at_starting(0)
print('After insertion at beginning, the linked list is :')
ll.print_list()

### inserting after the first node in linked list
ll.at_any_place(first, 101)
print('After insertion at any point, the linked list is :')
ll.print_list()

### inserting at the end of linked list
ll.at_ending(5896)
print('After insertion at the end, the linked list is :')
ll.print_list()