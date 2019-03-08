import sys

def main():
  n = int(sys.stdin.readline().strip())
  a = [1]
  s = 1
  if n == 0:
    print 1
    return
  # for n = 20, e is accurate to more than 15 decimal places
  for i in xrange(min(20,n),1,-1):
    a.append(a[-1]*i)
    s += a[-1]
  print "%.20f" % (s/(a[-1]*1.0) + 1)

if __name__ == '__main__':
  main()

