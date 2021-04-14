'''
    ### Problem statement:
            Reverse a doubly linked list.

    ### Time Complexity: O(n)

    ### Approach:
        Take three variables - previous, current and nxt
        Now, set previous = null, current and nxt = head
        then follow the below approach until nxt becomes null
                
                nxt = current->next
                current->next = previous
                current->prev = nxt
                previous = current
                current = nxt
'''

class Node:
    count = 0
    def __init__(self, data):
        # making two pointers prev and next
        self.data = data 
        self.next = None
        self.prev = None 
        Node.count += 1


class DLL:
    def __init__(self):
        # head to locate first node
        # tail to locate last node
        self.head = None 
        self.tail = None

    def push(self, val):
        node = Node(val)
        # if head is node i.e., linked list is empty
        # then point head and tail to the node
        if self.head is None:
            self.head = node 
            self.tail = node

        # else link the node to tail    
        else:
            self.tail.next = node 
            node.prev = self.tail 
            self.tail = node

    def traverse(self):
        # function to display element present in linked list
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print() 

    def reverse(self):
        previous = None
        curr = self.head 
        nxt = self.head 
        while nxt:
            nxt = curr.next
            curr.next = previous
            curr.prev = nxt 
            previous = curr 
            curr = nxt 
            
        # swapping head and tail so that traverse() function can work    
        temp = self.tail
        self.tail = self.head 
        self.head = temp 


ll = DLL()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.traverse()
print('After reversing the doubly linked list:')
ll.reverse()
ll.traverse()