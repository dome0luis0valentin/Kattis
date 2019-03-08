import sys
from fractions import Fraction as F
from collections import defaultdict

def bfs(graph, n, start=0):
  dist = [F(1) for i in xrange(n)]
  q = [(start, F(1))]
  seen = [False for i in xrange(n)]
  seen[start] = True
  while len(q) > 0:
    curr, d = q.pop()
    seen[curr] = True
    for u,w in graph[curr]:
      if not seen[u]:
        new_d = w*d
        seen[u] = True
        dist[u] = new_d
        q.append((u, new_d))
  return dist

def solve(graph, units, unit_map,n):
  weights = bfs(graph, n)
  unit_order = map(lambda x:x[1], sorted(zip(weights, units), key=lambda x: x[0]))
  weights =  map(int, bfs(graph, n, unit_map[unit_order[0]]))
  str_rep = []
  for u in unit_order:
    str_rep.append("{}{}".format(weights[unit_map[u]],u))
  print " = ".join(str_rep)

def main():
  line = lambda : sys.stdin.readline().strip()
  n = int(line())
  while n != 0:
    graph = defaultdict(list)
    units = line().split()
    unit_map = dict([(unit, i) for i,unit in enumerate(units)])
    for i in xrange(n-1):
      big, weighted_small = line().strip().split("=")
      weight, small = weighted_small.split()
      weight = int(weight)
      big, small = unit_map[big.strip()], unit_map[small]
      graph[big].append( (small, F(weight)) )
      graph[small].append( (big, F(1,weight)) )
    solve(graph, units, unit_map, n)
    n = int(line())
if __name__ == '__main__':
  main()
