import sys
from collections import defaultdict

def components(graph, unseen):
  if len(graph) == 0:
    return len(unseen)
  c = 0
  for n in unseen:
    if unseen[n]:
      q = [n]
      while len(q) > 0:
        v = q.pop()
        if unseen[v]:
          unseen[v] = False
          for i in graph[v]:
            q.append(i)
      c +=1
  return c



def main():
  getline = lambda : sys.stdin.readline().strip()
  line = getline()
  case = 1
  while line:
    rows, cols = [int(i) for i in line.split()]
    graph = defaultdict(list)
    prev = ["#"]*cols
    unseen = {}
    for r in xrange(rows):
      curr = list(getline())
      curr.append("#")
      for c in xrange(cols):
        if curr[c] == "-":
          pos = r*cols + c
          unseen[pos] =  True
          if (curr[c+1] == curr[c]):
            graph[pos].append(pos+1)
            graph[pos+1].append(pos)
          if (prev[c] == curr[c]):
            graph[pos].append(pos-cols)
            graph[pos-cols].append(pos)
      prev = curr

    print "Case {}: {}".format(case,components(graph, unseen))
    line = getline()
    case += 1

if __name__ == '__main__':
  main()
