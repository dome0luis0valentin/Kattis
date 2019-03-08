import sys
from collections import defaultdict

def main():
  n,q = [int(i) for i in sys.stdin.readline().split()]
  adds = defaultdict(lambda:0)
  for line in sys.stdin:
    line = line.split()
    if line[0] == '1':
      a,b,c = [int(i) for i in line[1:]]
      adds[(a,b)] += c
    else:
      D = int(line[1])
      s = 0
      for (a,b) in adds:
        if (D%b == a):
          s += adds[(a,b)]
      print s


if __name__ == '__main__':
  main()
