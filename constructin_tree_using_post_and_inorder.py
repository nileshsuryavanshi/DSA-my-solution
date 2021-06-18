'''
    ### Construction of binary tree using post-order and in-order.
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

def construct(postList, inList):   # O(n^2)
    if not postList or not inList:
        return None
    root = Node(postList[-1])
    mid = inList.index(postList[-1])
    root.left = construct(postList[:mid], inList[:mid])
    root.right = construct(postList[mid:-1], inList[mid+1:])
    return root

def construct2(postList, inList):  # O(n)
    if not postList or not inList:
        return None
    root = Node(postList[-1])
    inMap = dict(zip(inList, range(len(inList))))
    mid = inMap[postList[-1]]
    root.left = construct2(postList[:mid], inList[:mid])
    root.right = construct2(postList[mid:-1], inList[mid+1:])
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


# list containing post-order and in-order of a tree which we have to construct
postorder = [6, 8, 7, 4, 11, 12, 10, 9, 5, 2, 3, 1]
inorder = [6, 4, 8, 7, 2, 5, 11, 9, 12, 10, 1, 3]
root = construct(postorder, inorder)
inOrder(root)
print()
preOrder(root)
print()
postOrder(root)
print()
