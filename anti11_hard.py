import sys
M = (10**9) + 7

def solve(n,allergy):
  pass


def main():
  line = lambda : sys.stdin.readline().strip()
  t = int(line())
  for i in xrange(t):
    n, allergy = line().split()
    print solve(int(n), allergy)

if __name__ == '__main__':
  main()
