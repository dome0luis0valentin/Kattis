import sys,itertools

class Line:
    def __init__(self,x1,y1,x2,y2):
        # line is ax + by +c = 0
        self.a = (y2 - y1)
        self.b = (x1 - x2)
        self.c = y1*(x2-x1) + x1*(y1 - y2)

    @classmethod
    def from_points(cls,p1,p2):
        return cls(p1[0],p1[1],p2[0],p2[1])

    def in_line(self,x,y):
        return (self.a*x + self.b*y + self.c) == 0
    def contains(self,p):
        return (self.a*p[0] + self.b*p[1] + self.c) == 0


def are_colinear(triples):
    p1,p2,p3 = triples
    l = Line.from_points(p1,p2)
    if l.contains(p3):
        return l
    else:
        return None

def find_first_Line():
    points = []
    for i in range(5):
        points.append(tuple(int(i) for i in sys.stdin.readline().split()))

    for t_index in itertools.combinations(range(5),3):
        triples = (points[t_index[0]],points[t_index[1]],points[t_index[2]])
        poss_line = are_colinear(triples)
        if  poss_line != None:
            outside = []
            for p in points:
                if not poss_line.contains(p):
                    outside.append(p)
            return poss_line,outside

    return None,[]

def main():
    n = int(sys.stdin.readline().strip())
    l1,points = find_first_Line()
    if l1 == None:
        print "failure"
        return

    count = 1+len(points)
    while len(points) < 2:
        p = tuple(int(i) for i in sys.stdin.readline().split())
        if count == n-4:
            print "success"
            return
        if not l1.contains(p):
            points.append(p)
        else:
            count += 1

    l2 = Line.from_points(points[0],points[1])

    for line in sys.stdin:
        p = tuple(int(i) for i in line.split())
        if (not l1.contains(p)) and (not l2.contains(p)):
            print "failure"
            return

    print "success"

if __name__ == '__main__':
    main()
