import sys, math, Queue
from collections import defaultdict

def shortest(graph, start, end, n):
  time = [-1 for i in xrange(n+2)] # min time to travel from start to node n
  time[start] = 0
  pq = Queue.PriorityQueue()
  pq.put((0,start))
  while not pq.empty():
    t, curr = pq.get()
    for u, u_t in graph[curr]:
      if time[u] == -1 or t+u_t <time[u]: # found a better path
        time[u] = t+u_t
        pq.put((time[u],u))
  return time[end]


def main():
  line = lambda : sys.stdin.readline().strip()
  dist = lambda p1,p2: math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
  graph = defaultdict(list)
  start = map(float, line().split()) # start will be at index 0
  end = map(float, line().split()) # end will be at index 1
  n = int(line())

  # first creat an edge between start and end position
  t = dist(start, end)/5.0 # time it takes if you walk from start to end
  graph[0].append((n+1,t))
  graph[n+1].append((0,t))
  cannons = [map(float, line().split()) for i in xrange(n)]
  for i,c1 in enumerate(cannons):
    # distance detween cannon and endpoints
    d1, d2 = dist(c1, start), dist(c1, end)
    t1, t2 = d1/5.0, min(d2/5.0, 2 + abs(d2-50)/5.0)
    i +=1
    # start has node id  0, end has node id -1
    graph[i].append((0,t1))
    graph[0].append((i,t1))
    graph[i].append((n+1,t2))
    graph[n+1].append((i,t2))
    for i2 in xrange(i,n):
      c2, i2 = cannons[i2], i2+1
      d = dist(c1,c2)
      t = min(d/5.0, 2 + abs(d-50)/5.0)
      graph[i].append((i2, t))
      graph[i2].append((i, t))

  print shortest(graph, 0, n+1, n)

if __name__ == '__main__':
  main()
