'''
Given a binary tree, write a function to get the maximum width of the given tree.
The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree,
but some nodes are null.

The width of one level is defined as the length between the end-nodes
(the leftmost and right most non-null nodes in the level,
where the null nodes between the end-nodes are also counted into the length calculation.

### Time complexity: O(n)
'''

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None 

def maxWidth(root):
    if root:
        # if left and right node do not exit then print 1 and return
        if root.left is None and root.right is None:
            print(1)
            return 
        # queue to store node and index
        queue = [(root, 0)]
        m = 1
        size = 0
        while queue:
            popped = queue.pop(0)
            index = popped[1]
            m = m-1
            if popped[0].left:
                # left node index = (root node index)*2+1
                queue.append((popped[0].left, index*2+1))
            if popped[0].right:
                # right node index = (root node index)*2+2
                queue.append((popped[0].right, index*2+2))
            if m == 0:
                m = len(queue)
                if queue:
                    # get index of first and last element
                    # then assign size = last-first+1
                    first = queue[0][1]
                    last = queue[-1][1]
                    size = max(size, last-first+1)
        print(size)


'''
      1
     / \
    3   2
   /     \  
  5       9 
 /         \
6           7

We are going to find the maxWidth of above tree viz 8.
'''

root = Node(1)
root.left = Node(3)
root.left.left = Node(5)
root.left.left.left = Node(6)
root.right = Node(2)
root.right.right = Node(9)
root.right.right.right = Node(7)
# calling the function
maxWidth(root)