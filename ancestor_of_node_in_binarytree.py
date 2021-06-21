'''
    ### Finding ancestor of a node in binary tree.
    ### Time complexity: O(n)
'''
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None 

def ancestor(root, val):
    if root:
        if root.data == val:
            return True 
        if ancestor(root.left, val) or ancestor(root.right, val):
            print(root.data, end=' ')
            return True

'''
            1
          /   \
        /       \
       2         3
     /  \
   /      \
  4        5

We are going to use above tree.
'''

root = Node(1)
root.left = Node(2)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right = Node(3)
# finding ancestors of 5 which are 2 and 1
ancestor(root, 5)
print()