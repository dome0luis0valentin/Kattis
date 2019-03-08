import sys

def main():
  x = float(sys.stdin.readline().strip())
  c = 0
  if x == 10:
    print "No solution"
    return
  for i in xrange(1,9):
    for ai in xrange(1,10):
      n = round((10**(i) -1)/(10-x)*ai,4)
      if int(n) == n:
        n_p = str(int(n*x))
        if len(n_p) == i:
          print int(n)
          c += 1
  if c==0:
    print "No solution"

if __name__ == '__main__':
  main()
