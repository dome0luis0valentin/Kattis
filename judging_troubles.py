import sys
from collections import defaultdict

def main():
  getLine = lambda : sys.stdin.readline().strip()
  n = int(getLine())
  not_in = defaultdict(int)
  for i in xrange(n):
    not_in[getLine()] += 1
  for i in xrange(n):
    not_in[getLine()] -= 1
  print n - sum(map(lambda x: abs(x), not_in.values()))/2

if __name__ == '__main__':
  main()
