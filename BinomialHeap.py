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

    def setChildren(self, children):
        self.children = children

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
