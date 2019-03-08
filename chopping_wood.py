import sys
from heapq import heappush as push, heappop as pop
from collections import defaultdict

def main():
  n = int(sys.stdin.readline().strip())
  coming_up = defaultdict(int)
  vs = []
  leaves = set(range(1,n+2))
  for line in sys.stdin:
    v = int(line.strip())
    coming_up[v] += 1
    vs.append(v)
    if v in leaves:
      leaves.remove(v)

  if vs[-1] != n+1:
    print "Error"
    return

  avail = []
  for i in leaves:
    push(avail, i)

  soln = []
  for i in vs:
    if len(avail) == 0:
      print "Error"
      return
    soln.append(str(pop(avail)))
    coming_up[i] -= 1
    if coming_up[i] == 0:
      push(avail, i)

  print "\n".join(soln)

if __name__ == '__main__':
  main()
