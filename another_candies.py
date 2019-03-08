import sys

def main():
  line = lambda : sys.stdin.readline().strip()
  t = int(line())
  for i in xrange(t):
    line()
    n = int(line())
    total = 0
    for j in xrange(n):
      total += int(line()) % n
    if total % n == 0:
      print "YES"
    else:
      print "NO"

if __name__ == '__main__':
  main()
