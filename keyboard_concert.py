import sys
from collections import defaultdict

def main():
  getInts = lambda : map(int, sys.stdin.readline().split())
  n,m = getInts()
  key_board = defaultdict(set)
  for i in xrange(n):
    playables = getInts()[1:]
    for key in playables:
      key_board[key].add(i)
  notes = getInts()
  switches = 0
  curr = set(range(n))
  for k in notes:
    avail = key_board[k]
    curr = curr & avail
    if len(curr) == 0: # need a switch
      curr = avail
      switches += 1
  print switches

if __name__ == '__main__':
  main()
