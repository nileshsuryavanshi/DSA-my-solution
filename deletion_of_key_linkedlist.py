class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def delete(self, val):
        temp = self.head 
        
        # if the item to be deleted is at starting node
        '''
           agar element first node pe he to use delete karna he 
           aur head ko second node pe point karana hai
        '''
        if (temp is not None):
            if temp.data == val:
                self.head = temp.next 
                temp = None
                return
        
        # finding the item to delete
        '''
           search until the element to be deleted is found
        '''
        while (temp is not None):
            if temp.data == val:
                break 
            prev = temp
            temp = temp.next  

        # return if the item to be deleted is not found
        if temp == None:
            return 

        # unlink the node from the linked list
        prev.next = temp.next 
        temp = None 

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
ll.delete(2)
ll.print_list()
