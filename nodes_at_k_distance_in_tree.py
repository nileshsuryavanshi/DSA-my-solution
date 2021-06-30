'''
------------------------------------------------------------------------------------------------->
### Finding the nodes at k distance in a binary tree.
### Time complexity: O(n)
### Auxiliary space: O(h), where h is the height width of tree
------------------------------------------------------------------------------------------------->
'''
# class to create nodes of binary tree
class Node:
    def __init__(self, data):
        self.data = str(data) 
        self.left = self.right = None 

# function to find nodes at k distance
def nodesAt(k, count, root):
    if root:
        # if count == k then print the node value
        if count == k:
            print(root.data, end=' ')
        count += 1
        # do not exceed value of k
        if count <= k:
            # apply the same function on both side of node
            nodesAt(k, count, root.left)
            nodesAt(k, count, root.right)

'''
            1
          /   \
        /       \
       2         3
     /  \
   /      \
  4        5

We are going to use the tree above to find the nodes at k distance.
At 0 --> 1
At 1 --> 2, 3
At 2 --> 4, 5
'''

#creating tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# finding nodes at each of distance/level
for i in range(3):
    print(f'Elements at level {i} are :', end=' ')
    nodesAt(i, 0, root)
    print()
