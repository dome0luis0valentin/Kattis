import sys

def main():
  n,q = map(int, sys.stdin.readline().split())
  n +=2
  FT = [0 for i in xrange(n+1)]
  for line in sys.stdin:
    line = line.split()
    if line[0] == "+":
      index = int(line[1])+1
      delta = int(line[2])
      while(index <= n):
        FT[index] += delta
        index += index & (~(index - 1))
    else:
      index = int(line[1])
      s = 0
      while(index > 0):
        s += FT[index]
        index &= (index-1)
      print s

if __name__ == '__main__':
  main()
