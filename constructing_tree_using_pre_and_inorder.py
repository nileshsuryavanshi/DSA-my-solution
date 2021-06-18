'''
    ### Construction of binary tree using pre-order and in-order.
    ### Time complexity : 
                        For construct() function it is  : O(n^2)
                        For construct2() function it is : O(n)
                        
                        Note:-
                        In construct2() function we've used hashmap to find index of element in in-order list
                        which has O(1) time complexity for searching any element in most of the case. But, in very
                        few cases it has O(n).
'''

class Node:
    def __init__(self, data):
        self.data = str(data) 
        self.left = self.right = None 

def construct(preList, inList):   # O(n^2)
    if not preList or not inList:
        return None
    root = Node(preList[0])
    mid = inList.index(preList[0])
    root.left = construct(preList[1:mid+1], inList[:mid])
    root.right = construct(preList[mid+1:], inList[mid+1:])
    return root

def construct2(preList, inList):  # O(n)
    if not preList or not inList:
        return None
    root = Node(preList[0])
    inMap = dict(zip(inList, range(len(inList))))
    mid = inMap[preList[0]]
    root.left = construct2(preList[1:mid+1], inList[:mid])
    root.right = construct2(preList[mid+1:], inList[mid+1:])
    return root

# fuctions to check pre-order, in-order and post-order traversal for constructed binary tree
def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')


# list containing pre-order and in-order of a tree which we have to construct
preorder = [1, 2, 4, 6, 7, 8, 5, 9, 11, 10, 12, 3]
inorder = [6, 4, 8, 7, 2, 5, 11, 9, 12, 10, 1, 3]
root = construct(preorder, inorder)
inOrder(root)
print()
preOrder(root)
print()
postOrder(root)
print()
