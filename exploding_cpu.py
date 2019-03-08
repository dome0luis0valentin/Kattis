import sys, math, bisect

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
  return primes, nums

def is_prime(n, prime, mark):
  if n < len(mark):
    return mark[n]
  for p in prime:
    if p*p > n:
      break
    if n%p == 0:
      return False
  return True

def gen_all():
  primes, mark = sieve(11548) # sqrt(2*10**9/15)
  n = len(primes)
  exploding = []
  for i in xrange(1,n):
    p1 = primes[i]
    if p1 > 1260: # p1 can't be bigger than cubroot of 2*10^9
      break
    p1_sq = p1*p1
    for j in xrange(i+1,n):
      p2 = primes[j]
      if p2 % (p1-1) == 1:
        A = (p2-p1)/(p1-1)
        B = p1-A
        chain = [p1,p2]
        p = chain[-1]*A + B
        last = p1*p2
        while is_prime(p, primes, mark):
          last *= p
          if last > 2*(10**9):
            break
          exploding.append(last)
          p = A*p + B
  return sorted(exploding)

def main():
  n = int(sys.stdin.readline().strip())
  all_exploding = gen_all()
  for line in sys.stdin:
    low, high = map(int, line.split())
    lb = bisect.bisect(all_exploding, low-1)
    ub = bisect.bisect(all_exploding, high)
    print ub - lb


if __name__ == '__main__':
  main()
