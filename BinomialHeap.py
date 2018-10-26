import math

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
        if(self.children[0] == None):
            self.children[0] == child
        else:
            self.children.append(child)

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

    def __repr__(self):
        return "Node{ key : " + str(self.key) + ", value : " + str(self.value) + "}"


class BinomialTree:
    def __init__(self):
        self.root = None
        self.degree = 0

    def getDegree(self):
        return self.degree

    def getRoot(self):
        return self.root

    def upDegree(self):
        self.degree += 1

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
            self.root.upDegree()
        else:
            tree.getRoot().addChild(self.root)


    def __repr__(self):
        return self.printPart(self.root,0)

    def printPart(self,node,width):
        if(node==None):
             return "X"

        string=" "
        halfway=math.floor(len(node.getChildren())/2)
        for child in range(0,halfway):
            string+=self.printPart(node.getChildren()[child],width+3)
            string+="\n"+width*" "
        string+=width*" "
        string+=str(node.key)+"\n"
        for child in range(halfway,len(node.getChildren())):
            string+=self.printPart(node.getChildren()[child],width+3)
            string+="\n"+width*" "
        return string




class BinomialHeap:
    def __init__(self):
        self.trees = []



def main():
    binTree = BinomialTree()
    binTree.root = BinomialNode(4, "asdfasd", [BinomialNode(2, "ther", [BinomialNode(3, "there", [], None)], None), BinomialNode(6, "ther", [BinomialNode(3, "there", [], None)], None)], None)
    print(binTree)



if(__name__ == "__main__"):
    main()
