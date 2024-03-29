from BSTutils import TreeNode
"""
Problem
------------
Check if BST is valid.

Parameters
----------
root : TreeNode
    root of the tree.

Algorithm
---------

1.Start in root and range -inf(lower bound), inf(upper bound) - it will be valid 
2. Go to the left/right node and pass lower bound and value / value and upper bound check if node value is between 
this bounds if yes repeat till end of the tree for node childrens else Tree is invalid.

Complexity O(logn)

"""
def isValidBSTrek(root):
    def isValidNode(root, l, r):
        if not root:
            return True
        return l < root.val < r and isValidNode(root.left, l, root.val) and isValidNode(root.right, root.val,r)

    if not root:
        return True

    return isValidNode(root, float('-inf'), float('inf'))

def isValidBSTiter(root):
    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, l, r = stack.pop()

        if node == None:
            continue

        if not (l < node.data < r):
            return False

        stack.append((node.right, node.data, r))
        stack.append((node.left, l, node.data))

    return True

root = TreeNode(2,TreeNode(1),TreeNode(3))

isValidBSTiter(root)