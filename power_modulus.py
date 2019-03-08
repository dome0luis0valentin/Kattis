import sys

def main():
  a,b = [int(i) for i in sys.stdin.readline().split()]
  if a%2 == 0:
    print pow(a/2,b,a)
  else:
    print 0
if __name__ == '__main__':
  main()
