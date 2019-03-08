import sys
from array import array

def sieve(n):
  n +=1
  mark = array('B', (255 for i in xrange(n/8 + 1)))
  p = 2
  mark[0] ^= 1
  mark[0] &= ~(1<<1)
  while( p*p < n ):
    at,i = divmod(p,8)
    if mark[at] & 1<<i :
      for i in xrange(p*p, n, p):
        ai, ii = divmod(i,8)
        mark[ai] &= ~(1<<ii)
    p +=1

  count = 0
  for i in xrange(2,n):
    at,ii = divmod(i,8)
    if mark[at] & (1<<ii):
      count += 1

  return count,mark

def main():
  n,q = map(int, sys.stdin.readline().split())
  c,mask = sieve(n)
  print c
  for line in sys.stdin:
    at,i = divmod(int(line.strip()),8)
    print 1 if (mask[at] & (1<<i)) else 0

if __name__ == "__main__":
  main()

