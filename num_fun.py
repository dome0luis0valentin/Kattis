import sys

def main():
  n = int(sys.stdin.readline().strip())
  for i in xrange(n):
    a,b,c = [int(k) for k in sys.stdin.readline().strip().split()]
    if (a+b==c or a*b==c or a-b==c or b-a==c or a==b*c or b==a*c):
      print "Possible"
    else:
      print "Impossible"

if __name__ == "__main__" :
  main()
