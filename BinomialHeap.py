class BinomialNode:
    def __init__(self, key, value, children, parent):
        self.key = key
        self.value = value
        self.children = children #array
        self.parent = parent #node

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getChildren(self):
        return self.children

    def addChild(self, child):
        self.child.append(child)

    def deleteChild(self, child):
        index = self.children.index(child)
        if(index == -1):
            return None
        else:
            node = self.children[index]
            self.children.pop(index)
            return node

    # def setChildren(self, children):
    #     self.children = children

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


class BinomialTree:
    def __init__(self):
        self.root = None
        self.degree = 0

    def getDegree(self):
        return self.degree

    def getRoot(self):
        return self.root

    def upDegree(self):
        self.degree++;

    # def add(self, key, value):
    #     if (self.root == None):
    #         self.root = BinomialNode(key, value, [None], None)
    #     else:
    #         recursAdd(self.root, key, value)
    #
    # def recursAdd(self, node, key, value):
    #

    def merge(self, tree):
        if(self.root < tree.getRoot()):
            self.root.addChild(tree.getRoot())
            self.root.setDegree
        else:
            tree.getRoot().addChild(self.root)

class BinomialHeap:
    def __init__(self):
        self.heap
