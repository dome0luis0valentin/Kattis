import sys, math
from collections import defaultdict

def required(graph, n, k):
  target = 1
  curr, flow = n,k
  while curr != 1:
    parent,part,power = graph[curr]
    if power == 1:
      flow = math.sqrt(flow)
    flow = flow/part
    curr = parent
  return flow

def main():
  l = lambda : sys.stdin.readline().strip()
  n = int(l())
  graph = [(0,0,0) for i in xrange(n+1)]
  for x in xrange(n-1):
    a,b,x,t = [int(i) for i in l().split()]
    graph[b] = (a,(x/100.0),t)
  nodes = [int(i) for i in l().split()]
  total = []
  for n,k in enumerate(nodes):
    if k > 0:
      total.append(required(graph, n+1, k))
  print max(total)

if __name__ == '__main__':
  main()
