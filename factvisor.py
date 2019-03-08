import sys,math

NUM_MAX = 2**31

def sieve(n):
  marks = [True for i in xrange(n+1)]
  p = 2
  while (p*p < n):
    if marks[p]:
      for i in xrange(2*p, n+1, p):
        marks[i] = False
    p +=1

  primes = []
  for i in xrange(2,n+1):
    if marks[i]:
      primes.append(i)
  return primes

# can use this list of primes to factorize any number less than 2**31
PRIMES = sieve(int(math.sqrt(NUM_MAX))+1)

def factorize(n):
  facts = {}
  sqrt_n = int(math.sqrt(n))+1

  for p in PRIMES:
    if p < sqrt_n:
      multiplicity = 0
      while n%p == 0:
        n /=p
        multiplicity += 1
      if multiplicity > 0:
        facts[p] = multiplicity
        if n == 1:
          break
    else:
      break
  if n > 1:
    facts[n] = 1

  return facts

def how_many(n,p):
  # count how many powers of p there are in n!
  total = 0
  while (p <= n):
    n = n/p
    total += n
  return total

def factvis(n,m):
  # Return true if m divides n!
  if m==0:
    return False
  facts = factorize(m)
  for p in facts:
    if how_many(n,p) < facts[p]:
      return False
  return True

def main():
  for line in sys.stdin:
    n,m = [int(i) for i in line.strip().split()]
    if factvis(n,m):
      print "{} divides {}!".format(m,n)
    else:
      print "{} does not divide {}!".format(m,n)

if __name__ == '__main__':
  main()
