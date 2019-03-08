import sys

def main():
  m,a,b,c = [int(i) for i in sys.stdin.readline().split()]
  d = a+b+c
  if d > 2*m:
    print "impossible"
  else:
    print "possible"

if __name__ == '__main__':
  main()
