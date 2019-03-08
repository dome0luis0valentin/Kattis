import sys,math

def sieve(n):
  nums = [True for i in xrange(n)]
  p = 2
  while( p*p < n ):
    if nums[p]:
      for i in xrange(2*p, n, p):
        nums[i] = False
    p +=1

  primes = []
  for i in xrange(9,n):
    if nums[i]:
      primes.append(i)
  return primes

primes = range(1,10) + sieve(46340)

def find(n):
  if n == 0:
    return 4
  if n < 4:
    return -1
  sq = int(math.sqrt(n)) + 1
  second_half = []
  for p in primes:
    if n%p == 0:
      if p > 3:
        return p
      second_half.append(n/p)
  return second_half[-1]

def main():
  for line in sys.stdin:
    line = int(line.strip())
    if line == 0:
      return
    n = line - 3
    b = find(n)
    if b == -1:
      print "No such base"
    else:
      print b

if __name__ == "__main__":
  main()

