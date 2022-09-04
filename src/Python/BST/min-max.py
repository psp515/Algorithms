


def min(root):
    if root.left == None:
        return root

    iterable = root.left
    while iterable.left != None:
        iterable = iterable.left

    return iterable


def max(root):
    if root.right == None:
        return root

    iterable = root.right
    while iterable.right != None:
        iterable = iterable.right

    return iterable
