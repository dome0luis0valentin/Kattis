import sys, math

def main():
  cases = int(sys.stdin.readline().strip())
  for c in xrange(cases):
    p,r,f = [int(i) for i in sys.stdin.readline().split()]
    if p>f:
      print 0
    else:
      n = int(math.ceil(math.log((f*1.0)/p,r)))
      if p*(r**n) > f:
        print n
      else:
        print n+1

if __name__ == '__main__':
  main()

