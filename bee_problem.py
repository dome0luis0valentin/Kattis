import sys
from collections import defaultdict

def components(graph, nodes):
  seen = dict([(n, False) for n in nodes])
  comps = []
  visited = 0
  node_index = 0
  while len(nodes) > visited:
    while seen[nodes[node_index]]:
      node_index += 1
    q = [nodes[node_index]]
    comps.append(0)
    while len(q) > 0:
      curr = q.pop()
      if seen[curr]:
        continue
      seen[curr] = True
      comps[-1] += 1
      for n in graph[curr]:
        if not seen[n]:
          q.append(n)
    visited += comps[-1]
  return comps


def main():
  line = lambda : sys.stdin.readline()
  h, n, m = map(int, line().split())

  graph = defaultdict(list)
  row = line().split()

  nodes = []
  if row[0] == ".":
    nodes.append(0)

  for i in xrange(1,m):
    if row[i] == ".":
      nodes.append(i)
    if row[i] == row[i-1] == ".":
      graph[i].append(i-1)
      graph[i-1].append(i)

  prev = row
  parity,row = 0,0
  for line in sys.stdin:
    line = line.split()
    parity +=1
    row +=1
    for i in xrange(m):
      r1 = row*m + i
      if line[i] == ".":
        nodes.append(r1)
      if i > 0 and line[i] == line[i-1] == ".":
        r2 = r1 - 1
        graph[r1].append(r2)
        graph[r2].append(r1)
      if parity % 2 == 1:
        x1,x2 = i,i+1
      else:
        x1,x2 = i-1,i

      if 0<= x1 < m and prev[x1] == line[i] == '.':
        x = (row-1)*m +  x1
        graph[x].append(r1)
        graph[r1].append(x)
      if 0<= x2 < m and prev[x2] == line[i] == '.':
        x = (row-1)*m +  x2
        graph[x].append(r1)
        graph[r1].append(x)
    prev = line

  comps = sorted(components(graph, nodes))
  count  = 0
  while h > 0 and len(comps) > 0:
    h -= comps.pop()
    count +=1
  print count

if __name__ == '__main__':
  main()
