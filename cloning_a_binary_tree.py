'''
    ### Cloning a tree using preorder traversal.
    ### Time complexity : O(n)
'''

class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

def clone(root):
    if root:
        tree = Node(root.value)
        tree.left = clone(root.left)
        tree.right = clone(root.right)
        return tree 

def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

'''
            1
          /   \
        /       \
       2         3
     /  \
   /      \
  4        5

We are going to use tree given above and make a copy of it.
And will try to traverse it in preorder, postorder and inorder.
'''

root = Node(1)
root.left = Node(2)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right = Node(3)
print('Original tree traversals:-')        
print('Preorder:')
preorder(root)
print('\nPostorder:')
postorder(root)
print('\nInorder:')
inorder(root)
print()

clone_tree = clone(root)
print('\nClone tree traversals:-')        
print('Preorder:')
preorder(clone_tree)
print('\nPostorder:')
postorder(clone_tree)
print('\nInorder:')
inorder(clone_tree)
print()
