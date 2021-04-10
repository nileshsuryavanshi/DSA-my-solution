class Node:
    def __init__(self, val):
        self.data = val 
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def swap_node(self, x, y):
        # if both x and y are equal then return
        if x == y:
            return  

        # set previous nodes of x and y as null    
        prev_x = prev_y = None
        temp = self.head 

        # finding the prev and next node of x
        while temp.data != x and temp:
            prev_x = temp
            temp = temp.next

        curr_x = temp.data
        x_node = temp 
        next_x = temp.next

        temp = self.head 
        # finding the prev and next node of y
        while temp.data != y and temp:
            prev_y = temp 
            temp = temp.next 

        curr_y = temp.data 
        y_node = temp 
        next_y = temp.next 

        # if both the nodes found 
        if curr_x == x and curr_y == y:
            # if prev of y is x node
            if x_node == prev_y:
                if prev_x == None:
                    self.head = y_node
                    y_node.next = x_node
                    x_node.next = next_y
                else:
                    prev_x.next = y_node
                    y_node.next = x_node
                    x_node.next = next_y        
            
            # if x is the first node
            elif prev_x == None:
                self.head = y_node 
                y_node.next = next_x
                prev_y.next = x_node
                x_node.next = next_y 
            
            else:
                prev_x.next = y_node
                y_node.next = next_x 
                prev_y.next = x_node 
                x_node.next = next_y   

        # show message when any or both nodes not found         
        else:
            print('Both or one element are/is not there in linked list:)')                                    

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print()


ll = LL()

# making nodes
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

# linking nodes
ll.head = one 
one.next = two 
two.next = three
three.next = four 
four.next = five
five.next = six

# displaying the elements present in linked list
ll.display()
# performing swapping
ll.swap_node(4,6)
# displaying updated linked list after swapping
ll.display()