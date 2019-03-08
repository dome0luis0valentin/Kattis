import sys
M = (10**9) + 7

def solve(n,allergy):
  k = (len(allergy) - 1)
  if k+1 > n:
    return 2**n % M
  combs = [[] for i in xrange(2**k)]
  # Generate linear recurrence
  deci_allergy = int(allergy,2)
  m = 2**k
  for v in xrange(2**k):
    # Adding 0 & 1 to the end
    v0, v1 = 2*v, 2*v + 1
    if v0 != deci_allergy:
      combs[v0 % m].append(v)
    if v1 != deci_allergy:
      combs[v1 % m].append(v)

  curr = [1 for i in xrange(2**k)]
  next_ = []
  for i in xrange(k+1,n+1):
    for j in xrange(2**k):
      total = 0
      for c in combs[j]:
        total = (total + curr[c]) % M
      next_.append(total)
    curr, next_ = next_, []
  return sum(curr) % M

def main():
  line = lambda : sys.stdin.readline().strip()
  t = int(line())
  for i in xrange(t):
    n, allergy = line().split()
    print solve(int(n), allergy)

if __name__ == '__main__':
 main()
