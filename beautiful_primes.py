import sys

def main():
  cases = int(sys.stdin.readline().strip())
  for c in xrange(cases):
    n = int(sys.stdin.readline().strip())
    for i in xrange(n+1):
      val = (2**i) * (11**(n-i))
      if len(str(val)) == n:
        print " ".join(["2" if k < i else "11" for k in xrange(n)])
        break

if __name__ == '__main__':
  main()
