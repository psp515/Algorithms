

def next(root):
    # root has right subtree
    if root.right != None:
        iterable = root.right

        while iterable.left != None:
            iterable = iterable.left

        return iterable

    # if root is main root
    if root.parent == None:
        # if root is the biggest element
        if root.right == None:
            return None
        return root.right

    # root don't have right subtree
    iterable = root.parent
    while iterable.parent != None and iterable.parent.left != iterable:
        iterable = iterable.parent

    return iterable


def prev(root):
    # root has left subtree
    if root.left != None:
        iterable = root.left

        while iterable.right != None:
            iterable = iterable.right

        return iterable

    # if root is main root
    if root.parent == None:
        # if root is the biggest element
        if root.left == None:
            return None
        return root.left

    # root don't have right subtree
    iterable = root.parent
    while iterable.parent != None and iterable.parent.right != iterable:
        iterable = iterable.parent

    return iterable