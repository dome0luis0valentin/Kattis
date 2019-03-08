import sys
from collections import defaultdict

dependency_order = []
seen = set()

def topological_sort(graph, start):
  seen.add(start)
  for i in graph[start]:
      if i not in seen:
        topological_sort(graph,i)
  dependency_order.append(start)

def dfs(graph,start):
  path = []
  stack = [start]
  label = len(graph)
  result = {}
  while stack != []:
    for element in stack:
      if element not in result:
        result[element] = label
        label = label -1
    v = stack.pop()
    if v not in path: path.append(v)
    for w in reversed(graph[v]):
      if w not in path and not w in stack:
          stack.append(w)

  return path

def main():
  n = int(sys.stdin.readline().strip())
  graph = defaultdict(list)
  for i in xrange(n):
    rule = sys.stdin.readline()
    child, parents = [k.strip() for k in rule.split(":")]
    parents = parents.split()

    for p in parents:
      if p in graph:
        graph[p].append(child)
      else:
        graph[p] = [child]
  changed_file = sys.stdin.readline().strip()
  if n < 100:
    topological_sort(graph, changed_file)
    order = reversed(dependency_order)
  else:
    order = dfs(graph, changed_file)
  for i in order:
    print i

if __name__ == '__main__':
  main()
