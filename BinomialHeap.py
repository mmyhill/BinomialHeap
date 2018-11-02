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
        self.children.append(child)
        child.parent = self

    def deleteChild(self, child):
        index = self.children.index(child)
        if(index == -1):
            return None
        else:
            node = self.children[index]
            #self.children.pop(index), does this pop empty index or
            self.chlidren[index] = None;
            return node

    def isSame(self, node):#does this need to be recursive, to minimize cases in which nodes have same keys
    #and values? ie check that children & childrens match
        return node.getKey() == self.key and node.getValue() == self.value and node.getParent() == self.parent

    def getParent(self):
        return self.parent

    #wont need to use unless node in between is deleted
    def setParent(self, parent):
        self.parent = parent


class BinomialTree:
    def __init__(self, key, value):#must have min one node to have tree, make node
        self.root = BinomialNode(key, value, [], None)
        self.degree = 0

    def setRoot(self, root):
        self.root = root

    def getDegree(self):
        return self.degree

    def getRoot(self):
        return self.root

    def upDegree(self):
        self.degree += 1

    def setDegree(self, addDegree):
        self.degree += addDegree

    def __repr__(self):
        return self.printPart(self.root,0)

    def printPart(self,node,width):
        if(node==None):
             return "X"

        string=" "
        halfway=math.floor(len(node.getChildren())/2)
        for child in range(0,int(halfway)):
            string+=self.printPart(node.getChildren()[child],width+3)
            string+="\n"+width*" "
        string+=width*" "
        string+=str(node.key)+"\n"
        for child in range(int(halfway), int(len(node.getChildren()))):
            string+=self.printPart(node.getChildren()[child],width+3)
            string+="\n"+width*" "
        return string

    def merge(self, treeToMerge):#assuming trees are same degree
        if(self.root.getValue() > treeToMerge.getRoot().getValue()):
            treeToMerge.addChild(self)
        else:
            self.addChild(treeToMerge)

class BinomialHeap:
    def __init__(self, key, value):
        self.heap = [BinomialTree(key, value)]#array of trees


    # def add(self, key, value):
    #     new = BinomialTree(key,value)
    #     if (self.heap[0] == None):
    #         self.heap[0] = new
    #     else:
    #         self.addOrMerge(new)

    def add(self, key, value):
        newBinHeap = BinomialHeap(key, value)
        self.merge(binHeap)


    def merge(self, binHeap):

        newHeap = []
        i = 0
        j = 0
        #for(i in ran)





    # def addOrMerge(self, treeToAdd):#recursive & "private" method
    #     toComp = BinomialTree(None, None)
    #
    #     if(self.heap[treeToAdd.getDegree()] is None):#base case, no more merges
    #         self.heap[treeToAdd.getDegree()] = treeToAdd
    #         print("LOOK IF1", self.heap[treeToAdd.getDegree()])
    #
    #     if(treeToAdd.getRoot().getKey() >= toComp.getRoot().getKey()):
    #         toComp.getRoot().addChild(treeToAdd.getRoot())
    #         toComp.upDegree()
    #         print("LOOK IF2")
    #         if(self.heap[treeToAdd.getDegree()] is None):
    #             self.heap[treeToAdd.getDegree()] = treeToAdd
    #             print("LOOK IF3")
    #         else:
    #             self.addOrMerge(toComp)
    #             print("LOOK ELSE1")
    #
    #     else:#root of tree already in array is larger than tree being added
    #         treeToAdd.getRoot().addChild(toComp.getRoot())
    #         treeToAdd.upDegree()
    #         self.heap[toComp.getDegree()] = None
    #         self.addOrMerge(toComp)
    #         print("LOOK ELSE2")

    def get(self, key):#if there exist multiple nodes w/h same key, value and parent,
        pass
        #our code will return first from left, prob a detail we dont even need to worry about anyway
            # for i in range()

    def __repr__(self):
        printBoi = ""
        for i in self.heap:
            if i != None:
                printBoi += str(i)
                printBoi += '\n'#new line
        return printBoi

def main():
    binHeap = BinomialHeap()
    binHeap.add(2, "halkefjadsklfj")
    binHeap.add(4, "ha")
    binHeap.add(8, "hal")
    binHeap.add(6, "LOL")
    print(binHeap.heap)

if __name__ == "__main__":
    main()
