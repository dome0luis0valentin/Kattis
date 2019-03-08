import sys

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
  return primes,mark

primes,mark = sieve(2000)

def npf(n):
  facts = 1
  pf = 0
  for p in primes:
    if p*p > n or (n < 2000 and mark[n]):
      break
    c = 0
    while n%p == 0:
      c += 1
      n /= p
    if c>0:
      facts *= (c+1)
      pf += 1
  if n > 1:
    facts *=2
    pf +=1

  return facts -pf

def main():
  getInt = lambda : int(sys.stdin.readline().strip())
  n = getInt()
  lines = sys.stdin.readlines()
  ans = (str(npf(int(i.strip()))) for i in lines)
  sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
  main()

