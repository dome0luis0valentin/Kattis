class Node:
    def __init__(self,data):
        self.key = data
        self.classRep = None

    def setRep(self,a_node):
        self.classRep = a_nod

    def __eq__(self,other):
        if type(other) == type(self.key):
            return self.key == other
        return self.data == other.key

    def __ne__(self,other):
        return not self.__eq__(other)

    def __ge__(self,other):
        if type(self.key) == type(other):
            return self.key > other
        return self.key > other.key

    def __hash__(self):
        return self.key.__hash__()

class SubSets:
    def __init__(self):
        self.collection = []
        self.totalSets = 0

    def findRep(a_node):
        """
        Recursive method to find the representative of a node.
        After finding top rep, nodes are relinked to make further lookups
        easy.
        """
        if a_node.classRep == None:
            return a_node
        rep = findRep(a_node.classRep)
        a_node.setRep(rep)
        return rep

    def add(self,num1,num2):
        n1 = Node(num1)
        n2 = Node(num2)
        b1 = n1 in self.collection
        b2 = n2 in self.collection
        if  b1 == True and b2 == False :
            n2.setRep(n1)
            self.collection.append(n2)
        elif
