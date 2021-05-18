class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None

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

We are going to make the above tree with the help of code.
And will try to traverse it in preorder, postorder and inorder.
'''

root = Node(1)
root.left = Node(2)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right = Node(3)        
print('Preorder:')
preorder(root)
print('\nPostorder:')
postorder(root)
print('\nInorder:')
inorder(root)
print()