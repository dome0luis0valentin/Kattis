import sys

def count_tight(k,n):
  prev = [ 0 for i in xrange(k+3) ]
  curr = [ 0 for i in xrange(k+3) ]
  for i in xrange(k+1):
    prev[i+1] = 1
  for j in xrange(2,n+1):
    for e in xrange(k+1):
      curr[e+1] = prev[e] + prev[e+1] + prev[e+2]
    prev = list(curr)
  return sum(prev)


def main():
  for line in sys.stdin:
    k,n = [int(i) for i in line.split()]
    count = count_tight(k,n)
    print "%.9f" % ((count*100.0)/( (k+1)**n ))
if __name__ == '__main__':
  main()
