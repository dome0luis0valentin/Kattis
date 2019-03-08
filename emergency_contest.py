import sys

def main():
  n, fact = [int(i) for i in sys.stdin.readline().split()]
  n = n-1
  print n%fact + fact + 1 if 2*fact <= n else n

if __name__ == '__main__':
   main()
