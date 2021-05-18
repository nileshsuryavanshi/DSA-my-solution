'''
    ### Level order(bfs) binary tree traversal
        Time complexity ---  O(n)
        Space complexity --- O(n)

    Approach:
        Here we are going to use queue for breadth first traversal. We will enqueue each node one by one and deque them
        accordingly.
'''
class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None

def bfs(root):
    # first enqueue root node
    queue = [root]
    while len(queue) != 0:
        # dequeue root node and print its value
        rnode = queue.pop(0)
        print(rnode.value, end=' ')
        # enqueue left node of parent if available
        if rnode.left:
            queue.append(rnode.left)
        # enqueue right node of parent if available    
        if rnode.right:
            queue.append(rnode.right)

'''
            1
          /   \
        /       \
       2         3
     /  \
   /      \
  4        5

We are going to traverse above tree using bfs.
'''
root = Node(1)
root.left = Node(2)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right = Node(3)       
bfs(root)
print()