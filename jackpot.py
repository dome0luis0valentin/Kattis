import sys

def gcd(a,b):
  a,b = (a,b) if a>=b else (b,a)
  while b:
    a,b = b, a%b
  return a

def lcm(a,b):
  return (a*b)/gcd(a,b)

def main():
  line = lambda : sys.stdin.readline().strip()
  m = int(line())
  for i in xrange(m):
    line()
    period = reduce(lambda a,b: lcm(a,b),[int(k) for k in line().split()])
    if period > 10**9:
      print "More than a billion."
    else:
      print period


if __name__ == '__main__':
  main()
