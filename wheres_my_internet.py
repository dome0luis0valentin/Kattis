import sys

def reachable(graph, start,vertex_count):
  q = [start]
  visited = [False for i in xrange(vertex_count+1)]

  while(len(q) != 0):
    curr = q.pop()
    visited[curr] = True
    # if it has no neighbors
    if curr not in graph:
      continue
    for v in graph[curr]:
      if not visited[v]:
        q.append(v)

  count = 0
  for i in xrange(1,vertex_count+1):
    if not visited[i]:
      print i
      count += 1
  if count == 0:
    print "Connected"


def main():
  graph = {}
  n,m = [int(i) for i in sys.stdin.readline().split()]
  for line in sys.stdin:
    v1,v2 = [int(i) for i in line.split()]
    if v1 in graph:
      graph[v1].append(v2)
    else:
      graph[v1] = [v2]
    if v2 in graph:
      graph[v2].append(v1)
    else:
      graph[v2] = [v1]
  reachable(graph,1,n)

if __name__ == "__main__":
  main()
