'''
   ### 3. Floyd's cycle-finding algorithm:      
        -- Traverse linked list using two pointers.
        -- Move one pointer(slow_p) by one and another pointer(fast_p) by two.
        -- If these pointers meet at the same node then there is a loop. 
           If pointers do not meet then linked list doesn’t have a loop.
 
        ** This is the fastest method
           Here,
                time complexity --> O(n)
                auxiliary space --> O(1), No extra space is needed
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

    def detect_loop(self):
        slow = self.head
        fast = self.head 
        c = 0
        while (slow and fast and fast.next):
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                c = 1
                break  

        if c == 1:
            print('Found')
        else:
            print('Not found')         


ll = LinkedList()
one = Node(2)
two = Node(5)
three = Node(1)        
four = Node(4)       
ll.head = one 
one.next = two 
two.next = three 
three.next = four
# four.next = two
 
ll.detect_loop()
