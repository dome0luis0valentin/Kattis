import sys
from math import sin, cos
def main():
  p,a,b,c,d,n = [int(i) for i in sys.stdin.readline().split()]

  f = lambda k : sin(a*k + b) + cos(c*k + d)
  max_sofar = f(1)
  max_diff = 0
  for i in xrange(2,n+1):
    fi = f(i)
    diff = max_sofar - fi
    if fi > max_sofar:
      max_sofar = fi
    if diff > max_diff:
      max_diff = diff

  print "{:.7f}".format(max_diff*p)

if __name__ == '__main__':
  main()
