import sys
from collections import defaultdict

def dfs(graph, node, visited, leadToCycle, inPath=set()):
  visited[node] = True
  inPath.add(node)
  for v in graph[node]:
    if not visited[v]:
      if dfs(graph, v, visited, leadToCycle, inPath):
        leadToCycle[node] = True
        return True
    elif v in inPath or leadToCycle[v]:
      leadToCycle[node] = True
      return True
  inPath.remove(node)
  return False

def main():
  graph = defaultdict(list)
  n = int(sys.stdin.readline().strip())
  city_map = {}
  curr = 0
  for line in sys.stdin:
    c1,c2 = line.split()
    if c1 in city_map:
      c1 = city_map[c1]
    else:
      city_map[c1] = curr
      c1 = curr
      curr += 1
    if c2 in city_map:
      c2 = city_map[c2]
    else:
      city_map[c2] = curr
      c2 = curr
      curr += 1
    graph[c1].append(c2)
    n -= 1
    if n == 0:
      break

  visited = [False for i in xrange(curr+1)]
  leadToCycle = [False for i in xrange(curr+1)]
  for line in sys.stdin:
    city = line.strip()
    cid = city_map[city]
    if not visited[cid]:
      dfs(graph,cid,visited, leadToCycle)
    print "{} {}".format(city, "safe" if leadToCycle[cid] else "trapped")


if __name__ == '__main__':
  main()
