import sys

def main():
  line = lambda : sys.stdin.readline().strip()
  c,x,m = [float(i) for i in line().split()]
  left = c/2.0
  fastest = 0
  for i in xrange(6):
    s,eff = map(float, line().split())
    time = m/s
    used = m/eff + time*x
    if 2*used <= c:
      fastest = s
  if fastest > 0:
    print "YES",int(fastest)
  else:
    print "NO"

if __name__ == '__main__':
  main()
