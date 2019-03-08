import sys
from collections import defaultdict

def check(graph, node_vals):
  visited = [False]*len(node_vals)
  while True:
    start = -1
    for i,k in enumerate(visited):
      if not k:
        start = i
        break
    if start == -1:
      break
    q = set([start])
    total = 0
    while len(q) > 0:
      v = q.pop()
      total += node_vals[v]
      visited[v] = True
      for u in graph[v]:
        if not visited[u]:
          q.add(u)
    if total != 0:
      return False
  return True



def main():
  line = lambda : sys.stdin.readline().strip()
  n, m = [int(i) for i in line().split()]
  node_vals = [int(line()) for i in xrange(n)]
  graph = defaultdict(list)
  for i in xrange(m):
    a,b = [int(k) for k in line().split()]
    graph[a].append(b)
    graph[b].append(a)
  print "POSSIBLE" if check(graph,node_vals) else "IMPOSSIBLE"

if __name__ == '__main__':
  main()
