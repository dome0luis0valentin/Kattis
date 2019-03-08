import sys
from collections import defaultdict

def degree(s):
  n = len(s)
  for i in xrange(n-1,0,-1):
    sub_map = defaultdict(int)
    for k in xrange(n-i+1):
      sub = s[k:k+i]
      sub_map[sub] += 1
    if min(sub_map.values()) > 1:
      return i
  return 0

def main():
  for line in sys.stdin:
    print degree(line.strip())

if __name__ == '__main__':
  main()
