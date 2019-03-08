import sys
import bisect
from collections import defaultdict


def edge(i,j,graph, hardened):
  if j not in hardened and i not in hardened:
    graph[i].add(j)
    graph[j].add(i)

def bfs(start, end, graph, n):
  steps = 0
  curr, nxt = set([start]), set()
  while len(curr) + len(nxt) > 0:
    if len(curr) == 0:
      curr, nxt = nxt, set()
      steps += 1
    if steps > n:
      return "No"
    if end in curr:
      return steps
    q = curr.pop()
    for v in graph[q]:
        nxt.add(v)
  return "No"


def main():
  line = lambda : sys.stdin.readline().split()
  r, n, start, end, x = map(int, line())
  if x > 1:
    hardened = set(map(int, line()))
  else:
    hardened = set()
  tiers = [1]
  size = [r]
  switch = 1
  for k in xrange(2*r-2):
    tiers.append(tiers[-1]+size[-1])
    if switch < r :
      size.append(size[-1] + 1)
    else:
      size.append(size[-1] - 1)
    switch +=1

  max_row = 2*r - 1
  cells = r**3 - (r-1)**3
  graph = defaultdict(set)
  for i in xrange(1, cells):
    if i in hardened:
      continue
    nxt_row = bisect.bisect(tiers, i)
    curr_row = nxt_row - 1
    pos = i - tiers[nxt_row - 1]
    # first neighbor
    if pos != 0:
      edge(i, i-1, graph, hardened)
    if pos + 1 < size[curr_row]:
      edge(i, i+1, graph, hardened)
    # 2nd and 3rd
    if nxt_row < max_row:
      if nxt_row < r:
        edge(i, tiers[nxt_row] + pos, graph, hardened)
        edge(i, tiers[nxt_row] + pos + 1, graph, hardened)
      if nxt_row >= r and pos > 0:
        edge(i, tiers[nxt_row] + pos - 1, graph, hardened)
      if nxt_row >= r and pos + 1 < size[curr_row]:
        edge(i, tiers[nxt_row] + pos, graph, hardened)

  print bfs(start, end, graph, n)

if __name__ == '__main__':
  main()
