import sys
from heapq import heappush as push, heappop as pop
from heapq import heapify

def main():
  k, n = [int(i) for i in sys.stdin.readline().strip().split()]
  queue = []
  for index in xrange(n+k-1):
    year, strength = [int(i) for i in sys.stdin.readline().strip().split()]
    queue.append((year, strength, index==0))

  queue.sort()
  contestants = [(-j[1], j[2]) for j in queue[:k]]
  heapify(contestants)
  karl_won, c = False, 0
  while(not karl_won):
    karl_won = pop(contestants)[1]   # winner
    c += 1
    if (c < n):
      _, ns, kw = queue[k+c-1]           # new contestant
    else:
      break
    push(contestants, (-ns, kw))

  print 2010+c if karl_won else "unknown"

if __name__ == '__main__':
  main()

