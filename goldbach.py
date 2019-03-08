import sys

def sieve(n):
  mark = [True for i in xrange(n+1)]
  p = 2
  while( p*p <= n ):
    if mark[p]:
      for i in xrange(2*p, n+1, p):
        mark[i] = False
    p +=1

  primes = []
  for i in xrange(2,n+1):
    if mark[i]:
      primes.append(i)
  return primes, mark

primes,marks = sieve(32000)

def goldbachs(n):
  reps = []
  for p in primes:
    if p>n/2:
      break
    elif marks[n-p]:
      reps.append("%d+%d"%(p,n-p))
  print "{0} has {1} representation(s)".format(n,len(reps))
  for rep in reps:
    print rep
  print



def main():
  n = int(sys.stdin.readline().strip())
  for case in xrange(n):
    goldbachs(int(sys.stdin.readline().strip()))

if __name__ == "__main__":
  main()
