import sys
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict

def get_shorty(graph, n):
  height = [-1.0 for i in xrange(n)]
  pq = []
  height[0] = 1.0
  hpush(pq, (height[0]*-1, 0))
  while len(pq) > 0:
    h, curr = hpop(pq)
    h = -1*h
    for n,w in graph[curr]:
      new_height = h*w
      if height[n] == -1 or new_height > height[n]:
        height[n] = new_height
        hpush(pq, (new_height*-1, n))
  return "{:.4f}".format(height[-1])


def main():
  line = lambda : sys.stdin.readline().split()
  n,m = map(int, line())
  while not (n == m == 0):
    graph = defaultdict(list)
    for e in xrange(m):
      n1, n2, w = line()
      n1, n2 = int(n1), int(n2)
      w = float(w)
      graph[n1].append((n2, w))
      graph[n2].append((n1, w))
    print get_shorty(graph, n)
    n,m = map(int, line())

if __name__ == '__main__':
  main()
