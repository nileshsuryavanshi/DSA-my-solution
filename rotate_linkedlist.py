'''
   Time complexity = O(n)
'''

class Node:
    count = 0
    def __init__(self, val):
        self.data = val 
        self.next = None
        Node.count += 1

class LL:
    def __init__(self):
        self.head = None


    def rotate(self, position):
        # if position is less than size of linked list
        # and is positive
        if position < Node.count and position >= 0:
            k = 0
            temp = self.head
            while temp.next:
                if k == position - 1:
                    prev = temp
                    nest = temp.next 
                if position == 0:
                    return    
                temp = temp.next
                k += 1
            prev.next = None
            temp.next = self.head
            self.head = nest       
        # if position is negative or more than linked list size
        # then return     
        else:
            return


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print()    

ll = LL()
one = Node(5)
two = Node(6)
three = Node(3)
four = Node(8)
five = Node(9)
six = Node(10)
ll.head = one 
one.next = two 
two.next = three
three.next = four 
four.next = five 
five.next = six 

ll.display()
ll.rotate(3)
ll.display()
