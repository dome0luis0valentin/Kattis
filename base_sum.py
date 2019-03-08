import sys
from fractions import gcd

def ds(n,b):
  s = 0
  while n:
    s += n%b
    n /= b
  return s

def ns(base,k,a):
  nums = set()
  for i in xrange(0,(a-1)*16):
    n = base + i
    diff = n - ds(n,a)
    if diff /(a-1)  == k:
      nums.add(n)
  return nums

def base_sum(n,a,b):
  while True:
    n += 1
    if ds(n,a) == ds(n,b):
      print n
      return

def main():
  base_sum(*[int(i) for i in sys.stdin.readline().split()])


if __name__ == '__main__':
  main()
