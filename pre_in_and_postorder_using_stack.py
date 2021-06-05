'''
    ### Traversing binary tree using iterative method, which will use stack.
    ### Time complexity : O(n)

    ### Video link to understand : https://www.youtube.com/watch?v=12aMTS0L6WI
'''

class Node:
    def __init__(self, data):
        self.data = str(data) 
        self.left = None
        self.right = None

class Pair:
    # this class will make a pair of node and state
    def __init__(self, node, state):
        self.node = node 
        self.state = state 

def iterativeTraversing(root):
    stack = [Pair(root, 1)]
    pre_ = ''       # to store nodes value in preorder
    in_ = ''        # to store nodes value in inorder
    post_ = ''      # to store nodes value in postorder
    while stack:
        top = stack[-1]
        # if state == 1, then :=  add to preorder, state++, go to left
        if top.state == 1:
            pre_ += top.node.data + ' '
            top.state += 1
            if top.node.left:
                lp = Pair(top.node.left, 1)
                stack.append(lp)

        # if state == 2, then :=  add to inorder, state++, go to right
        elif top.state == 2:
            in_ += top.node.data + ' '
            top.state += 1
            if top.node.right:
                rp = Pair(top.node.right, 1)
                stack.append(rp)

        # if state == 3, then :=  add to postorder, pop
        else:
            post_ += top.node.data + ' '
            stack.pop()    

    print('Preorder :', pre_)
    print('Inorder :', in_)
    print('Postorder :', post_)


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.left.right = Node(6)
root.right = Node(3)
root.right.left = Node(7)
root.right.right = Node(8)
root.right.right.right = Node(9)
iterativeTraversing(root)