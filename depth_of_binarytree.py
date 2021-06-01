'''
    ### Finding the depth/height of a binary tree.
    ### Time complexity = O(n)
'''

class Node:
    def __init__(self, data):
        self.data = data   
        self.left = None
        self.right = None

def depth(root):
    if root is None:
        # if node is null then return 0
        return 0
    else:
        # else return the max(ldepth, rdepth)
        ldepth = depth(root.left)
        rdepth = depth(root.right)
        if ldepth > rdepth:
            return ldepth+1 
        else:
            return rdepth+1

'''
            1
          /   \
        /       \
       2         3
     /  \
   /      \
  4        5

We will find out the height of above tree viz 3.
'''

root = Node(1)
root.left = Node(2)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right = Node(3) 
print('The depth of tree is :', depth(root))