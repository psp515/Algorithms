class TreeNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.parent = parent
        self.left = left
        if left != None:
            left.parent = self
        self.right = right
        if right != None:
            right.parent = self
        self.data = data


class ExtendedTreeNode:
    def __init__(self, data, parent=None):
        self.parent = parent
        self.childrens = []
        self.data = data