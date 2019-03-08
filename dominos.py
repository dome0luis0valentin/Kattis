import sys
from collections import defaultdict

class IdentityDict(dict):
  def __missing__(self,key):
    return key

graph = defaultdict(list)
round = 0
seen = []
topple_order = IdentityDict()

def order_vertex(v):
  global topple_order,graph,seen,round
  q = [v]
  while q:
    curr = q.pop()
    topple_order[curr] = round
    round -=1
    seen[curr] = True
    for v in graph[curr]:
      if not seen[v]:
        q.append(v)

def topple(graph,n,poss_starts):
  visited = [False for i in xrange(n)]
  unreached = set(range(n))
  start_count = 0
  while( len(unreached) > 0 ):
    start = poss_starts.pop()
    if visited[start]:
      continue

    q = [start]
    while (len(q) > 0):
      curr = q.pop()
      if curr in unreached:
        unreached.remove(curr)
      visited[curr] = True
      for v in graph[curr]:
        if not visited[v]:
          q.append(v)
    start_count +=1

  print start_count

def main():
  global round,graph,seen,topple_order
  cases = int(sys.stdin.readline().strip())
  for case in xrange(cases):
    n,m = [int(i) for i in sys.stdin.readline().split()]
    # Reset globals
    graph = defaultdict(list)
    topple_order = defaultdict(list)
    round = 0
    seen = [False for i in xrange(n)]
    for e in xrange(m):
      v1,v2 = [int(i)-1 for i in sys.stdin.readline().split()]
      graph[v1].append(v2)

    last = 0
    for i in xrange(n):
      if not seen[i]:
        round = last
        order_vertex(i)
        last +=1

    poss_starts = range(n)
    poss_starts.sort(key=lambda x:topple_order[x])
    topple(graph,n,poss_starts)


if __name__ == '__main__':
  main()

