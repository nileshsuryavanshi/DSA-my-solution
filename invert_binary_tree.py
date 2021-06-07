class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def invertTree(root):
    '''
    firstly, we will swap left and right node of root node
    then recursively call it for left node and right node
    '''
    if root:
        temp = root.left
        root.left = root.right 
        root.right = temp 
        invertTree(root.left)
        invertTree(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ') 
        inOrder(root.right)

root = Node(1)
root.left = Node(2)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right = Node(3)     
print("Before inverting-")   
print('Inorder:')
inOrder(root)        
print('\n\nAfter inverting-')
invertTree(root)
print('Inorder:')
inOrder(root)
print()