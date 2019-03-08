import sys

def count(keys, k, n):
  M = 1000000007
  ans = [0 for i in xrange(n+1)]
  fact = 1
  for i in xrange(k,n+1):
    ans[i] = (ans[i-1] + keys[i-1]*fact) % M
    fact = ((fact*i)/(i-k+1))
  return ans[-1] % M


def main():
  ints = lambda : sys.stdin.readline().split()
  n,k = map(int, ints())
  nums = map(int, ints())
  nums.sort()
  print count(nums, k, n)
if __name__ == '__main__':
  main()
