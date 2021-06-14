'''
    ### Inorder traversal using morris method.
    ### Time complexity : O(n) , Space complexity : O(1)
'''

class Node:
    def __init__(self, data):
        self.data = data 
        self.right = self.left = None

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

def morrisInorderTraversal(root):
    # setting inorder predecessor to null
    temp = None
    while root:
        # if left of current node exists then find the right most node
        if root.left:
            temp = root.left
            while temp.right and temp.right != root:
                temp = temp.right
            # if the right of predecessor is root
            # then set right of predecessor to null
            # and update root node to it's right
            if temp.right:
                temp.right = None 
                print(root.data, end=' ')
                root = root.right 
            # if right of predecessor is null
            # then set it's right to root
            # and update root node to it's left
            else:
                temp.right = root 
                root = root.left
        # if left of current node doesn't exist then print current node value
        # and update the node to it's right
        else:
            print(root.data, end=' ')
            root = root.right
    print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.left.right.left = Node(8)
root.left.right.right = Node(9)
root.left.right.right.left = Node(11)
root.left.right.right.right = Node(10)
root.left.right.right.right.left = Node(12)

print('Traversal using recursion:')
inOrder(root)
print('\nTraversal using morris method:')
morrisInorderTraversal(root)