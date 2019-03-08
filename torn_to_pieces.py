import sys
from collections import defaultdict

def path(graph, start, end):
  q = [start]
  prev = dict(zip(graph.keys(),graph.keys()))
  seen = dict([(k,False) for k in graph.keys()])
  if end not in seen:
    print "no route found"
    return

  found = False
  while len(q) > 0:
    curr = q.pop()
    if curr == end:
      found = True
      break
    if seen[curr]:
      continue
    seen[curr] = True
    for n in graph[curr]:
      if not seen[n]:
        q.append(n)
        prev[n] = curr

  if not found:
    print "no route found"
    return

  # now get path
  path = []
  n = end
  while n != start:
    path.append(n)
    n = prev[n]
  path.append(start)
  print " ".join(reversed(path))

def main():
  getLine = lambda : sys.stdin.readline().strip()
  n = int(getLine())
  graph = defaultdict(set)

  for i in xrange(n):
    line = getLine().split()
    init = line[0]
    for s in line[1:]:
      graph[init].add(s)
      graph[s].add(init)
  start, end = getLine().split()

  path(graph, start, end)

if __name__ == '__main__':
  main()
