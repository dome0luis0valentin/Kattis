import sys

def count(graph,q,visited):
    res = 0
    for curr in q:
        if curr not in visited:
            visited.add(curr)
            res += (1 + count(graph,graph[curr],visited))
    return res


def main():
    n = int(sys.stdin.readline().strip())
    graph = [[] for i in xrange(n+1)]

    boxes = sys.stdin.readline().split()
    for b in range(len(boxes)):
        b_parent = int(boxes[b])
        if b_parent:
            graph[b_parent].append(b+1)

    q = int(sys.stdin.readline().strip())
    for i in xrange(q):
        queries = [int(i) for i in sys.stdin.readline().split()][1:]
        print count(graph,queries,set())



if __name__ == '__main__':
    main()
