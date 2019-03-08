import sys, bisect

def main():
  n,m = [int(i) for i in sys.stdin.readline().split()]
  sizes = sorted([int(sys.stdin.readline().strip()) for i in xrange(n)])

  wasted = 0
  for c in sys.stdin:
    c = int(c.strip())
    wasted += sizes[bisect.bisect_left(sizes,c)] - c
  print wasted

if __name__ == '__main__':
  main()

