'''
#### 1. Hashing approach:
        Here we will store address of each node and see if it is available in our list or not,
        if it is available then there is a loop otherwise not.
        
        Here, 
        time complexity is  --> O(n)
        space complexity is --> O(n), because we are using a list to store address of each node.
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

    def check_loop(self):
        temp = self.head
        address = []
        flag = 0
        while temp:
            ad = id(temp)
            if ad in address:
                flag = 1
                break  
            address.append(ad)
            temp = temp.next    
        if flag == 1:
            print('There is a loop in the linked list.')
        else:
            print('There is no loop in the linked list.') 

    def remove_loop(self):
        temp = self.head
        address = []
        while temp:
            ad = id(temp)
            if ad in address:
                temp.next.next = None 
                break  
            address.append(ad)
            temp = temp.next                               

ll = LinkedList()
one = Node(2)
two = Node(5)
three = Node(1)        
four = Node(4)       
ll.head = one 
one.next = two 
two.next = three 
three.next = four
four.next = three
'''
  2-->5-->1-->4
          ^   |    here, time complexity is  --> O(n)
          !---!          space complexity is --> O(n), because we are using a list to store address of each node.
''' 
ll.check_loop()
ll.remove_loop()
ll.print_ll()
