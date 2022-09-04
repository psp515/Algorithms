from BSTutils import TreeNode

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