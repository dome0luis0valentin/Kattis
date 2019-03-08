import sys
from itertools import permutations

def sieve(n):
  n +=1
  nums = [True for i in xrange(n)]
  p = 2
  while( p*p < n ):
    if nums[p]:
      for i in xrange(2*p, n, p):
        nums[i] = False
    p +=1

  primes = []
  for i in xrange(2,n):
    if nums[i]:
      primes.append(i)
  return primes

PRIMES = sieve(3163) # sqrt(10**7)

def is_prime(n):
  if n<2:
    return False
  for p in PRIMES:
    if p*p > n:
      break
    if n%p == 0:
      return False
  return True

def count_primes(chars):
  seen = set()
  for length in xrange(1,len(chars)+1):
    for perm in permutations(chars,length):
      v = int("".join(perm))
      if v not in seen and is_prime(v):
        seen.add(v)
  return len(seen)

def main():
  next(sys.stdin)
  for line in sys.stdin:
    chars = line.strip()
    print count_primes(chars)

if __name__ == "__main__":
  main()

