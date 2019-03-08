import sys

def sod(n):
  s = 0
  while n!= 0:
    s += n%10
    n /=10
  return s

def cumulative_sum(n):
  s_n = 1
  a_n = 1
  sols = {1:1}
  for i in xrange(2,n+1):
    print i-1,a_n, a_n/9
    sd = sod(a_n)
    a_n += sd
  print i,a_n, a_n/9

def main():
  cumulative_sum(int(sys.argv[1]))
if __name__ == '__main__':
  main()

