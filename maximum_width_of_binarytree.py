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
    if root:
        # if left and right node do not exit then print 1 and return
        if root.left is None and root.right is None:
            print(1)
            return 
        # breadth first search
        queue = [root]
        # variable m will help us to know the completion of a level so that
        # we can update the size when a level completes
        m = 1
        size = 0
        # iterate until queue gets empty
        while queue:
            popped = queue.pop(0)
            m = m-1
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
            # update the size when m==0 i.e., a level completes
            if m == 0:
                m = len(queue)
                size = max(size, m)
        print(size)


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