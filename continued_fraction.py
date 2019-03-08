import sys

def gcd(a,b):
  a,b = (a,b) if a>b else (b,a)
  while b > 0:
    a,b = b, a%b
  return a

def continued(r):
  a,b = r
  elems = []
  while b != 0:
    q,r = divmod(a,b)
    a,b = b,r
    elems.append(str(q))
  return elems

def rational(elems):
  curr = (elems[-1], 1)
  elems.pop()
  while len(elems) > 0:
    a = elems.pop()
    b,c = curr
    curr = (a*b + c, b)
  return curr

def add(a,b,c,d):
  g = gcd(b,d)
  e1 = a*(d/g)
  e2 = c*(b/g)
  n,d = e1+e2, b*d/g
  g2 = gcd(n,d)
  return (n/g2, d/g2)

def mult(a,b,c,d):
  e1, e2 = a*c, b*d
  g = gcd(e1,e2)
  return (e1/g, e2/g)

def main():
  getInts = lambda : map(int, sys.stdin.readline().split())
  n,m = getInts()
  a,b = rational(getInts())
  c,d = rational(getInts())

  s = continued(add(a,b,c,d))
  diff = continued(add(a,b,-1*c,d))
  m = continued(mult(a,b,c,d))
  div = continued(mult(a,b,d,c))

  print " ".join(s)
  print " ".join(diff)
  print " ".join(m)
  print " ".join(div)

if __name__ == '__main__':
  main()
