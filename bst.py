import sys
import random
class Node:
    def __init__(self,data,left=None,right=None):
        self.key = data
        self.counter = 1
        self.left = left
        self.right = right
    def hasChild(self,pos=0): # by default checks left child
        if pos == 0: # 0 is left child
            return (self.left != None)
        else:
            return (self.right != None)

class BST:
    def __init__(self):
        self.root = None;
    def insert(self,key):
        if self.root == None:
            self.root = Node(key)
        else:
            self._insert(key,self.root)
    def _insert(self,key,p):
        if key < p.key: # should go left
            if (p.hasChild()) :
                self._insert(key,p.left)
            else:
                p.left = Node(key)
        elif key > p.key:
            if (p.hasChild(1)):
                self._insert(key,p.right)
            else:
                p.right = Node(key)
        else: # Tree already has the required Node
            p.counter +=1
    def str_rep(self):
        self._str_rep(self.root)
        print
    def _str_rep(self,p):
        # in order traversal
        if p==None:
            return
        self._str_rep(p.left)
        for i in range(p.counter):
            print p.key,
        self._str_rep(p.right)
    def peek(self):
        return self.root.key
    def lvls(self):
        return self._lvls(self.root)
    def _lvls(self,p):
        if p==None:
            return 0
        if not (p.hasChild() or p.hasChild(1)):
            return 1
        else:
            return max(self._lvls(p.left), self._lvls(p.right)) + 1

def main():
        n = int(sys.argv[1])
        a_tree = BST()
        for i in range(n):
            num = random.randint(0, n)
            a_tree.insert(num)
        a_tree.str_rep()
        print a_tree.lvls()
        print a_tree.peek()

if __name__ == '__main__':
    main()
