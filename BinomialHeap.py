from utils import new_array, new_int_array #how do arrays work w/o this? + how do I initialize this?
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
        return node.getKey() == self.key && node.getValue() == self.value &&
        node.getParent() == self.parent #do you use == to compare non numbers?

    def getParent(self):
        return self.parent

    #wont need to use unless node in between is deleted
    def setParent(self, parent):
        self.parent = parent


class BinomialTree:
    def __init__(self, key, value):#must have min one node to have tree, make node
        self.root = BinomialNode()
        self.degree = 0

    def setRoot(self, root):
        self.root = root

    def getDegree(self):
        return self.degree

    def getRoot(self):
        return self.root

    def upDegree(self):
        self.degree++;

    def setDegree(self, addDegree):
        self.degree += addDegree

class BinomialHeap:
    def __init__(self):
        self.heap #array of trees

        def add(self, key, value):
            new = BinomialTree(key,value)
           if (self.heap[0]) is None:
               self.heap[0] = new
            else:
                addOrMerge(self, new)

        def addOrMerge(self, treeToAdd):#recursive & "private" method
            if(self.heap[treeToAdd.getDegree()] is None):#base case, no more merges
                self.heap[treeToAdd.getDegree()] = treeToAdd

            toComp = self.heap[treeToAdd.getDegree()]#tree to merge with

            if(treeToAdd.getRoot().getKey() >= toComp.getRoot().getKey()):
                toComp.getRoot().addChild(treeToAdd.getRoot())
                toComp.upDegree()
                self.heap[treeToAdd.getDegree()] = None
                addOrMerge(toComp)

            else:#root of tree already in array is larger than tree being added
                treeToAdd.getRoot().addChild(toComp.getRoot())
                treeToAdd.upDegree()
                self.heap[toComp.getDegree()] = None
                addOrMerge(toComp)

        def get(self, key):#if there exist multiple nodes w/h same key, value and parent,
        #our code will return first from left, prob a detail we dont even need to worry about anyway
            for i in range()
