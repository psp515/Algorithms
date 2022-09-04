# BST

# succesor/predecessor

def succ(x):
    # Find minimum node in right subtree (left subtree for predecessor)
    if x.right:
        node = x.right
        while node and node.left:
            node = node.left
        return node

    # Find a node, which is a left child of a parent (right child for predecessor)
    node = x.parent
    while node:
        if node.left == x:
            break
        x = node
        node = node.parent

    return node


# Segment tree from lecture

class Node():
    def __init__(self, value, l, r) -> None:
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.value = value


class SegmentTree():
    def __init__(self, arr) -> None:
        self.arr = arr
        self.root = Node(0, 0, len(arr)-1)
        self.construct_tree()

    def construct_tree(self):
        def traverse(node, l, r, arr):
            if l == r:
                # One node
                node.value = arr[l]
                return node.value

            mid = l + (r - l)//2
            node.left = Node(0, l, mid)
            node.right = Node(0, mid + 1, r)

            s1 = traverse(node.left, l, mid, arr)
            s2 = traverse(node.right, mid + 1, r, arr)

            node.value = s1 + s2
            return node.value

        return traverse(self.root, 0, len(self.arr)-1, self.arr)

    def query(self, l, r):
        def traverse(node, l, r):
            if l <= node.l and node.r <= r:
                return node.value
            elif node.r < l or node.l > r:
                return 0
            else:
                return traverse(node.left, l, r) + traverse(node.right, l, r)

        return traverse(self.root, l, r)

    def update(self, l, r, x):
        def traverse(self, node, l, r, x):
            if not node:
                return
            if node.r < l or node.l > r:
                return node.value

            if node.l == node.r:
                self.arr[node.l] += x
                node.value += x
                return self.arr[node.l]

            s1 = traverse(self, node.left, l, r, x)
            s2 = traverse(self, node.right, l, r, x)
            node.value = s1 + s2
            return node.value
        traverse(self, self.root, l, r, x)

class MinimumSegmentTree():
    def __init__(self, arr) -> None:
        self.arr = arr
        self.root = Node(0, 0, len(arr)-1)
        self.construct()

    def construct(self):
        # Typowo jak w binary searchu
        def traverse(node, l, r, arr):
            if l == r:
                node.value = arr[l]
                return node.value

            mid = l + (r - l)//2

            node.left = Node(0, l, mid)
            node.right = Node(0, mid+1, r)

            s1 = traverse(node.left, l, mid, arr)
            s2 = traverse(node.right, mid+1, r, arr)

            node.value = min(s1, s2)
            return node.value

        traverse(self.root, 0, len(self.arr)-1, self.arr)

    def update(self, l, r, x):
        def traverse(self, node, l, r, x):
            if not node:
                return
            if node.r < l or node.l > r:
                return node.value

            if node.l == node.r:
                self.arr[node.l] += x
                node.value += x
                return self.arr[node.l]

            s1 = traverse(self, node.left, l, r, x)
            s2 = traverse(self, node.right, l, r, x)
            node.value = min(s1, s2)
            return node.value
        traverse(self, self.root, l, r, x)

    def query(self, l, r):
        def traverse(node, l, r):
            if l <= node.l and node.r <= r:
                return node.value

            if node.r < l or node. l > r:
                return float('inf')

            return min(traverse(node.left, l, r), traverse(node.right, l, r))
        return traverse(self.root, l, r)

x = MinimumSegmentTree([1, 1, 1, 1, 1, 1])
print(x.update(1, 3, 5))
print(x.update(2, 4, 2))
print(x.update(0, 0, -1))
# [1, 6, 8, 8, 3, 1]
print(x.query(1, 3))
print(x.arr)


class Node():
    def __init__(self, value, l, r):
        self.l = l
        self.r = r
        self.value = value
        self.left = None
        self.right = None
class RangeFreqQuery:

    def __init__(self, arr):
        self.arr = arr
        self.root = Node(0, 0, len(arr)-1)
        self.construct()

    def construct(self):
        def traverse(node, l, r):
            nonlocal self
            if l == r:
                node.value = {self.arr[l]: 1}
                return node.value

            mid = l + (r-l)//2
            node.left = Node(0, l, mid)
            node.right = Node(0, mid+1, r)

            dict1 = traverse(node.left, l, mid)
            dict2 = traverse(node.right, mid+1, r)

            # Merge dicts
            new_dict = {}
            for key in dict1:
                new_dict[key] = dict1[key]

            for key in dict2:
                if key in new_dict:
                    new_dict[key] += dict2[key]
                else:
                    new_dict[key] = dict2[key]

            node.value = new_dict
            return node.value
        traverse(self.root, 0, len(self.arr)-1)

    def query(self, left: int, right: int, value: int) -> int:
        def traverse(node, l, r, value):
            if l <= node.l and node.r <= r:
                if value in node.value:
                    return node.value[value]
                return 0

            if node.r < l or node.l > r:
                return 0

            return traverse(node.left, l, r, value) + traverse(node.right, l, r, value)

        return traverse(self.root, left, right, value)
