import sys

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

PRIMES = sieve(46341) # sqrt(2**31)

def factorize(n):
  facts = []
  if n < 0:
    facts.append((-1, 1))
    n *= -1

  for p in PRIMES:
    if p*p > n or  n==1:
      break
    count = 0
    while n%p == 0:
      n/=p
      count +=1
    if count > 0:
      facts.append((p,count))
  if n > 1:
    facts.append((n,1))

  f = map(lambda x: "{}^{}".format(x[0],x[1]) if x[1] > 1 else str(x[0]),facts)
  return " ".join(f)

def main():
  for line in sys.stdin:
    print factorize(int(line.strip()))

if __name__ == "__main__":
  main()

