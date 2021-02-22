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

    def swap(self, x, y):
        # if both the values are same then return
        if x == y:
            print('Both the key are same')
            return

        i = j = 0

        # finding the nodes which contain x and y
        temp = self.head 
        while temp:
            if temp.data == x:
                one = temp 
                i = 1
            elif temp.data == y:
                two = temp
                j = 1
            temp = temp.next 

        # check if any one or both value are present, if not present then return
        if (i == 0) or (j == 0):
            print("One or both element are not present in linked list")
            return

        # swapping x with y    
        one.data = y  
        two.data = x
        

# creating linked list object
ll = LinkedList()
print('Put the values for linked list : ')
take = list(map(int, input().split()))

# making and linking nodes
for i, val in enumerate(take):
    node = Node(val)
    if i == 0:
        ll.head = node 
    else:
        temp.next = node 
    temp = node          

# calling swap function
ll.swap(11,50)
ll.print_ll()
print()