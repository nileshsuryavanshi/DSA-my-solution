'''
    ### Calculating the diameter of binary tree.
    ### Time complexity : O(n)
'''
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None

def diameter(root):
    # base case
    if not root:
        return (0, 0)
    # calculate left and right height with diameter    
    lh = diameter(root.left)
    rh = diameter(root.right)
    height = max(lh[0], rh[0])+1
    # getting maximum diameter
    m['dia'] = max(m['dia'], lh[0]+rh[0]+1)
    return (height, m['dia'])

# creating a tree with 5 nodes with height 3
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# diactionary which will point to maximum diameter
m = dict(dia=0)
print('Height of the tree is:', diameter(root)[0])
print('Diameter of the tree is:', diameter(root)[1])