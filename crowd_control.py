import sys, Queue
from collections import defaultdict

def best_path(graph, n):
  dist = [0 for i in xrange(n)]
  prev = range(n)
  dist[0] = float("-inf")
  pq = Queue.PriorityQueue()
  pq.put((dist[0],0))
  while not pq.empty():
    du, u = pq.get()
    for v,w in graph[u]:
      new_dist = max(w,du) if du != 0 else w
      if dist[v] > new_dist:
        dist[v] = new_dist
        pq.put((dist[v], v))
        prev[v] = u

  curr = n-1
  path_edges = set([(n-1, prev[n-1])])
  path_nodes = set([n-1])
  while curr != 0:
    curr = prev[curr]
    path_nodes.add(curr)
    path_edges.add((curr, prev[curr]))

  return path_nodes, path_edges

def main():
  n,m = map(int, sys.stdin.readline().split())
  graph = defaultdict(list)
  edges = []
  for line in sys.stdin:
    u,v,w = map(int, line.split())
    w *= -1
    graph[u].append((v,w))
    graph[v].append((u,w))
    edges.append((u,v))

  path_n, path_e = best_path(graph, n)
  final = []
  for i,e in enumerate(edges):
    n1,n2 = e
    if (e not in path_e and (n2,n1) not in path_e) and (n1 in path_n or n2 in path_n):
      final.append(str(i))

  if len(final) == 0:
    print "none"
  else:
    print " ".join(final)

if __name__ == '__main__':
  main()
