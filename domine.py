import sys

def find_maximal(sums,k,occupied=set([])):
  pass

def main():
  n,k = [int(i) for i in sys.stdin.readline().split()]
  rows = []
  for line in sys.stdin:
    rows.append([int(i) for i in line.split()])
  print find_maximal(sums,k)

if __name__ == '__main__':
  main()
