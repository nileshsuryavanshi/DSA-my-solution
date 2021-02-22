'''
   ### 2. Detecting loop in linked list by modifying the structure of each node:
          Here we will add a flag to each node and assign it 0. While iterating through
          we will increase the value of flag and by checking the flag value we will find
          that loop is there or not.

          Here,
               time complexity --> O(n)
               auxiliary space --> O(1), No extra space is needed
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        ### adding one more paramter to node
        self.flag = 0


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
        temp = self.head
        c = 0
        while temp:
            if temp.flag == 1:
                c = 1
                break  
            temp.flag = 1
            temp = temp.next

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
