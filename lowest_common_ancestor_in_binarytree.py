'''
    ### Finding lowest common ancestor of two nodes in a binary tree.
    ### Time complexity: O(n)
'''
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None 

def lca(root, a, b):
    if not root:
        return None
    if root.data == a or root.data == b:
        return root
    l = lca(root.left, a, b)
    r = lca(root.right, a, b)
    if l and r:
        return root 
    return l if l else r

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
# lca for 4 and 5 is 2
lca_node = lca(root, 4, 5)
print(lca_node.data)