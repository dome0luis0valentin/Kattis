import sys
from collections import defaultdict

def royal_blood(q, graph, founder):
  if q == founder:
    return 1.0

  total = 0.0
  for p in graph[q]:
    total += royal_blood(p, graph, founder)/2.0
  return total

def main():
  line = lambda : sys.stdin.readline().strip()
  n, m = map(int, line().split())
  founder = line()
  fam_graph = defaultdict(list)
  for i in xrange(n):
    child, p1, p2 = line().split()
    fam_graph[child] = [p1,p2]

  heir, best_rb = "", -1
  for q in xrange(m):
    q = line()
    rb = royal_blood(q, fam_graph, founder)
    if rb > best_rb:
      heir, best_rb = q, rb
  print heir

if __name__ == '__main__':
  main()
