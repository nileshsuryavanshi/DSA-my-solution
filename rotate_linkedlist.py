'''
   Time complexity = O(n)
'''

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

    def length(self):
        temp = self.head 
        i = 0
        while temp:
            temp = temp.next
            i += 1    
        return i

    def rotate(self, k):
        current = self.head 
        next_k = None
        count = 1
        if k == self.length():
            '''
               return if the value of k is equal to the length of linked list
            '''
            return

        while current:
            if count == k:
                next_k = current.next 
                current.next = None
                break 
            current = current.next
            count += 1
        current = next_k    
        while current.next:
            current = current.next 
        current.next = self.head
        self.head = next_k         


ll = LinkedList()
one = Node(7)
two = Node(5)
three = Node(9)        
four = Node(4)
five = Node(6)       
ll.head = one 
one.next = two 
two.next = three 
three.next = four
four.next = five

ll.rotate(1)
ll.print_ll()