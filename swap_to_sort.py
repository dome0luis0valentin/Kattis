import sys
from collections import defaultdict

def component(graph, start, comps, val):
  q = [start]
  while len(q) > 0:
    u = q.pop()
    comps[u] = val
    for v in graph[u]:
      if comps[v] == 0: # haven't assigned comp val
        q.append(v)

def main():
  n,e = map(int,sys.stdin.readline().split())

  graph = defaultdict(list)
  for line in sys.stdin:
    v1,v2 = map(int, line.split())
    graph[v1].append(v2)
    graph[v2].append(v1)

  comps = [0]*(n+1)
  v = 1
  for i in xrange(1,n/2 + 1):
    j = n - i + 1
    if comps[i] == 0:
      component(graph, i, comps, v)
      v +=1
    if comps[i] != comps[j]:
      print "No"
      return
  print "Yes"

if __name__ == '__main__':
  main()
