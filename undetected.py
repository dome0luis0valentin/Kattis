import sys

WIDTH = 200
HEIGHT = 300

def intersect(c1,c2):
    x1,y1,r1 = c1
    x2,y2,r2 = c2
    return (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2


class Node:
    def __init__(self,key,c,parent = None,rank = 0):
        self.key = key
        self.parent = parent
        self.rank = rank
        self.left  = c[0] - c[-1] if c[0]-c[-1] > 0 else 0
        self.right = c[0] + c[-1] if c[0]+c[-1] < WIDTH else WIDTH
    def inc_rank(self):
        self.rank += 1
    def set_p(self,p):
        p.left = min(self.left,p.left)
        p.right = max(self.right,p.right)
        self.parent = p
    @property
    def fill(self):
        return self.right - self.left >= WIDTH
    def __repr__(self):
        return str(self.key)

class Tree:
    def __init__(self):
        self.sets = {}

    def add_set(self,i,c):
        self.sets[i]= Node(i,c)

    def find(self,a):
        # here a is a number

        return self._find(self.sets[a])

    def _find(self,a):
        # here a is a Node
        if a.parent == None or a.key == a.parent.key:
            return a
        p = self._find(a.parent)
        a.set_p(p)
        return a.parent
    def union(self,a,b):
        p1 = self.find(a)
        p2 = self.find(b)

        if p1.rank > p2.rank:
            p2.set_p(p1)
        elif p1.rank < p2.rank:
            p1.set_p(p2)
        else:
            p1.set_p(p2)
            p2.inc_rank()

def main():
    #sys.stdin = open(sys.argv[1],"r")
    n = int(sys.stdin.readline().strip()) # number of sensors
    disjoint_tree = Tree()
    sensors = []
    for i in range(n):
        c = tuple([int(j) for j in sys.stdin.readline().split()])
        sensors.append(c)
        disjoint_tree.add_set(i,c)
        for s in range(len(sensors)):
            sens = sensors[s]
            if intersect(sens,c):
                disjoint_tree.union(i,s)

        if disjoint_tree.find(i).fill:
            print i
            break


if __name__ == '__main__':
    main()
