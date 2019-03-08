import sys

def main():
  n,k = map(int, sys.stdin.readline().split())
  traveled = 1
  while n > k:
    q,r = divmod(n,k)
    if r == 0:
      n -= q
    else:
      n -= (q+1)
    traveled += 1
  print traveled + n

if __name__ == '__main__':
  main()
