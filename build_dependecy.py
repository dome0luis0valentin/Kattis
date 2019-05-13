import sys
from collections import defaultdict

def main():
  n = int(sys.stdin.readline().strip())
  graph = defaultdict(list)
  degrees = {}
  zeros = set()
  for i in xrange(n):
    rule = sys.stdin.readline()
    child, parents = [k.strip() for k in rule.split(":")]
    parents = parents.split()
    degrees[child] = len(parents)
    if degrees[child] == 0:
      zeros.add(child)
    for p in parents:
      graph[p].append(child)
  changed_file = sys.stdin.readline().strip()
  if changed_file in zeros:
    zeros.remove(changed_file)
  # Remove non startfile dependecy
  while zeros:
    curr = zeros.pop()
    for n in graph[curr]:
      degrees[n] -= 1
      if degrees[n] == 0 and n != changed_file:
        zeros.add(n)

  # Topological Sort
  zeros = [changed_file]
  while zeros:
    curr = zeros.pop()
    print curr
    for n in graph[curr]:
      degrees[n] -= 1
      if degrees[n] == 0:
        zeros.append(n)



if __name__ == '__main__':
  main()
