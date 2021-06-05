'''
    ### Preorder tree traversal using stack.
    ### Time complexity: O(n)
'''
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def preOrder(root):
    # firstly push the root node
    stack = [root]
    # iterate until stack becomes empty
    while stack:
        # pop current and print 
        current = stack.pop()
        print(current.data, end=' ')
        # push right node if exists and then left node if exists
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    print() 

'''
            1
          /   \
        /       \
       2         3
     /  \
   /      \
  4        5

We are going to make the above tree with the help of code.
And will try to traverse it in preorder.
'''

root = Node(1)
root.left = Node(2)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right = Node(3)    
# calling the function
preOrder(root)