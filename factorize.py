import sys, math

def sieve(n):
  n +=1
  mark = [True for i in xrange(n)]
  p = 2
  while( p*p < n ):
    if mark[p]:
      for i in xrange(2*p, n, p):
        mark[i] = False
    p +=1

  primes = []
  for i in xrange(2,n):
    if mark[i]:
      primes.append(i)
  return primes, mark

primes, is_prime = sieve(10000)

def factors(n):
  if n<10000 and is_prime[n]:
    return set([1,n])
  for p in primes:
    if p*p > n:
      break
    if n%p == 0:
      partial = factors(n/p)
      new_facts = set([])
      for fact in partial:
        new_fact = p*fact
        if new_fact not in partial:
          new_facts.add(new_fact)
      return new_facts.union(partial)
  return set([1,n])


def main():
  print factors(int(sys.argv[1]))

if __name__ == "__main__":
  main()

