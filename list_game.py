import sys,math

def sieve(n):
  nums = [True for i in xrange(n+1)]
  p = 2
  while( p*p <= n ):
    if nums[p]:
      for i in xrange(2*p, n+1, p):
        nums[i] = False
    p +=1

  primes = []
  for i in xrange(2,n+1):
    if nums[i]:
      primes.append(i)
  return primes

def main():
  n = int(sys.stdin.readline().strip())
  primes = sieve(int(math.sqrt(n)))
  count = 0

  for i in primes:
    while(n%i == 0):
      n /= i
      count +=1
    if (n==1):
      break
  if (n != 1):
    print  count + 1
  else:
    print  count

if __name__ == "__main__":
  main()
