import sys, math
from heapq import heappush as push, heapreplace as replace, heappop as pop

def main():
  n,k = map(int, sys.stdin.readline().split())
  min_heap = []
  pos = 1
  for order,line in  enumerate(sys.stdin):
    count, name = line.split()
    q = (int(count)*pos, -1*pos, name)
    if len(min_heap) < k:
      push(min_heap, q)
    elif min_heap[0] < q:
      replace(min_heap, q)
    pos += 1

  soln = []
  while len(min_heap) > 0:
    soln.append(pop(min_heap)[-1])
  print "\n".join(reversed(soln))

if __name__ == '__main__':
  main()
