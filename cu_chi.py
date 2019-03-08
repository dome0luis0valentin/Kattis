import sys

def main():
  getLine = lambda : sys.stdin.readline().strip()
  n = int(getLine())
  tree = [int(i) for i in getLine().split()]

  v = tree[0] # number of children it can carry
  for i in tree[1:]:
    v -= 1
    if v < 0:
      break
    v = v + (i-1)

  if v == 0:
    print "YES"
  else:
    print "NO"

if __name__ == '__main__':
  main()
