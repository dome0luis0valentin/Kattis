import sys
from fractions import gcd

def rotate(graph,n):
    curr_dir = [0 for i in xrange(n)]
    q = [0]
    curr_dir[0] = 1
    while(len(q)>0):
        v = q.pop()
        for u in graph[v]:
            if curr_dir[u]*curr_dir[v] == 1:
                return -1,-1
            elif curr_dir[u] == 0:
                q.append(u)
                curr_dir[u] = -1*curr_dir[v]
    if curr_dir[n-1] == 0:
        return 0,0
    else:
        return 1,curr_dir[-1]


def main():
    n = int(sys.stdin.readline().strip())
    gears = []
    graph = {}
    for i in xrange(n):
        x,y,r  = [int(k) for k in sys.stdin.readline().split()]
        gears.append((x,y,r))
        graph[i] = []
        for j in xrange(i):
            x1,y1,r1 = gears[j]
            d = (x1-x)**2 + (y1-y)**2
            if d == (r1+r)**2:
                graph[j].append(i)
                graph[i].append(j)
    d1,d2 = rotate(graph,n)
    if d1 == 1:
        g = gcd(gears[0][-1],gears[-1][-1])
        print (gears[-1][-1])/g, (gears[0][-1]*d2)/g
    else:
        print d1

if __name__ == '__main__':
    main()
