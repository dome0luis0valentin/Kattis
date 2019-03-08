import sys, math

def solve(n):
  D = len(n)
  num = long(n)
  if num == 0:
    return 0
  pow10 = 10**(D-8)
  for d in xrange(D-7, D+1):
    pow10_2 = 10*pow10
    if d*pow10 <= num < (d+1)*pow10_2:
      D = d
      break
    pow10 = pow10_2
  return num/D

def main():
  n = sys.stdin.readline().strip()
  print solve(n)

if __name__ == '__main__':
  main()
