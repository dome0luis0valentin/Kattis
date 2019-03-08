import sys

def judge(x,y,n):
  cx,cy = x,y
  x,y = 0,0
  for i in xrange(n):
    x,y = x*x-y*y+cx, 2*x*y+cy
    if x*x + y*y > 4:
      return False
  return True

def main():
  c = 1
  for line in sys.stdin:
    x,y,n = [float(i) for i in line.split()]
    verdict = "IN" if judge(x,y,int(n)) else "OUT"
    print "Case {}: {}".format(c, verdict)
    c +=1

if __name__ == '__main__':
  main()
