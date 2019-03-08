import sys

MOD = 1000000007

def f(n):
  v = 0
  while n>1:
    if n%2 == 0:
      n /= 2
    else:
      n += 1
    v += 1
  return v

def s(n):
  if n < 1:
    return 0
  if n%2 == 0:
    return (3*(n/2) - 2) + 2*s(n/2) % MOD
  else:
    return s(n-1) + f(n) % MOD

def main():
  n,m = [int(i) for i in sys.stdin.readline().split()]
  print (s(m) - s(n-1)) % MOD

if __name__ == '__main__':
  main()
