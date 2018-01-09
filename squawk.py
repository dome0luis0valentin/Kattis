import sys

graph = {}

def propagate(s,iterations,n):
    global graph
    prev_squaks = [0 for k in xrange(n+1)]
    squawks = [0 for k in xrange(n+1)]
    prev_squaks[s] = 1
    currently_infected = set([s])
    next_infected = set()
    for m in xrange(iterations):
        next_infected = set()
        squawks = [0 for k in xrange(n+1)]
        for i in currently_infected:
            for nei in graph[i]:
                squawks[nei] += prev_squaks[i]
            next_infected |= graph[i] # next all nighbours will be infected
        prev_squaks,squawks = squawks,prev_squaks
        currently_infected,next_infected = next_infected,currently_infected
    return sum(prev_squaks)
def main():
    global graph
    n,m,s,t = [int(i) for i in sys.stdin.readline().split()]
    graph = dict([(i,set()) for i in xrange(n+1)])
    for i in xrange(m):
        x,y = [int(j) for j in sys.stdin.readline().split()]
        graph[x].add(y)
        graph[y].add(x)

    print propagate(s,t,n)

if __name__ == '__main__':
    main()
