import sys,math

def main():
  getLine = lambda : sys.stdin.readline().strip()
  t = int(getLine())
  for i in xrange(t):
    n = int(getLine())
    points = 0
    for j in xrange(n):
      x,y = [int(k) for k in getLine().split()]
      D = x*x + y*y
      d = math.sqrt(D)
      inclosing = int(math.ceil(d/20.0))
      if inclosing > 10:
        points += 0
      elif inclosing == 0:
        points += 10
      else:
        points += (11-inclosing)
    print points

if __name__ == '__main__':
  main()
