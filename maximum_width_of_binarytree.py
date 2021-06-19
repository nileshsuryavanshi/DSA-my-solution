'''
------------------------------------------------------------------------------------------------->
### Finding the maximum width of a binary tree.
### Approach: We are going to use breadth first traversal of tree to find the maximum
              width of tree
### Time complexity: O(n)
### Auxiliary space: O(w), where w is the maximum width of tree
------------------------------------------------------------------------------------------------->
'''

class Node:
    def __init__(self, data):
        self.data = str(data) 
        self.left = self.right = None 

def getWidth(root):
    # maximum width will be the maximum size of queue
    if root:
        queue = [root]
        width = 1
        while queue:
            popped = queue.pop(0)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
            # updating width if new width is greater than previous one
            if len(queue) > width:
                width = len(queue)
        print('The maximum width of the given tree is :', width)


# making tree with maximum width of 4
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# calling the function
getWidth(root)