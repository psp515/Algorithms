from BSTutils import ExtendedTreeNode

class StringChainsTree():
    def __init__(self):
        self.root = ExtendedTreeNode("")


    def insert(self, word):
        iterable = self.root
        for letter in word:
            for i in range(len(iterable.childrens)):
                child = iterable.childrens[i]
                if letter == child:
                    iterable.data += 1
                    iterable = iterable.childrens[i]
                else:
                    iterable.childrens.append(ExtendedTreeNode(letter))
                    iterable = iterable.childrens[-1]
                    iterable.data = 1

    def contains_word(self, word):
        iterable = self.root
        for letter in word:
            for i in range(len(iterable.childrens)):
                child = iterable.childrens[i]
                if letter == child:
                    iterable = iterable.childrens[i]
                else:
                    return False

        return True