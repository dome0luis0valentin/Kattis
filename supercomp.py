import sys,math

class Node:
    def __init__(self,start,end,_sum=0):
        self._sum = _sum
        self.start = start  # start of a range
        self.end = end      # end of the range
        self.left = None
        self.right = None
    def add(self,val):
        self._sum += val
    def __repr__(self):
        return "<"+str(self.start)+", "+str(self.end)+"--"+str(self._sum)+">"


class SegmentTree:
    def __init__(self,n):
        self.currVal = [0]*n
        self.root = self.constructTree(0,n-1)

    def constructTree(self,start,end):
        if end == start :
            return Node(start,end)

        mid = (end+start)/2
        # no need to sum since out intial array is all 0
        root = Node(start,end)
        left_seg = self.constructTree(start,mid)
        right_seg = self.constructTree(mid+1, end)

        root.left = left_seg
        root.right = right_seg
        return root

    def getSum(self,lower,upper):
        return self._getSum(self.root,lower,upper)

    def _getSum(self,p,lower,upper):

        if p==None or p.start > upper or p.end < lower:
            return 0
        elif p.start <= lower and p.end >= upper:
            return p._sum
        else:
            mid = (lower+upper)/2
            right_sum = self._getSum(p.right,lower,upper)
            left_sum  = self._getSum(p.left, lower,upper)
            return right_sum + left_sum

    def updateVal(self,index):
        if self.currVal[index] == 0:
            diff = 1
            self.currVal[index] = 1
        else:
            diff = -1
            self.currVal[index] = 0
        self._updateVal(self.root,index,diff)

    def _updateVal(self,p,index,diff):

        if p==None or p.start > index or p.end < index:
            return

        p.add(diff)

        self._updateVal(p.left,index,diff)
        self._updateVal(p.right,index,diff)

    def show(self):
        self._show(self.root)
    def _show(self,p):
        if  p==None:
            return
        print p
        self._show(p.left)
        self._show(p.right)


def main():
    n,m = [int(k) for k in sys.stdin.readline().split()]
    seg_tree = SegmentTree(n+1)
    for line in sys.stdin:
        line = line.split()
        if line[0] == "F":
            seg_tree.updateVal(int(line[-1]))
        else:
            print " ".join(line).c
            print seg_tree.getSum(int(line[1]),int(line[-1]))



if __name__ == '__main__':
    main()
