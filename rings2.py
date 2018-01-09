import sys,math

def maximal_component(graph,n):
    components = {}
    comp_id = 0
    visited = [False for i in xrange(n)]
    max_count = 0
    for i in xrange(n):
        if not visited[i]:
            comp_id +=1
            components[comp_id] = set([i])
            q = set([i])
            while (len(q)>0):
                v = q.pop()
                visited[v] = True
                for u in graph[v]:
                    if not visited[u]:
                        components[comp_id].add(u)
                        q.add(u)
        if max_count < len(components[comp_id]):
            max_count = len(components[comp_id])

    return max_count;

def main():
    n = int(sys.stdin.readline().strip())
    while(n!=-1):
        circles = []
        graph = {}
        for i in xrange(n):
            cx,cy,cr = [float(k) for k in sys.stdin.readline().split()]
            circles.append((cx,cy,cr))
            graph[i] = []
            for j in xrange(i):
                cx2,cy2,r2 = circles[j]
                d = (cx-cx2)**2 + (cy-cy2)**2
                if d <= (cr+r2)**2 and d >= (cr-r2)**2:
                    graph[i].append(j)
                    graph[j].append(i)
        c = maximal_component(graph,n)
        print "The largest component contains",c,("ring." if c==1 else "rings.")
        n = int(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()
