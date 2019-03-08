import sys

def gcd(x,y):
  while(y):
    x,y = y, x%y
  return x

def main():
  getInts = lambda : map(int,sys.stdin.readline().split())
  n,k = getInts()
  min_mult = reduce(gcd, getInts()+[360])
  for q in getInts():
    if q%min_mult == 0:
      print "YES"
    else:
      print "NO"

if __name__ == '__main__':
  main()

