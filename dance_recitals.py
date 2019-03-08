import sys
from itertools import permutations

# Exhaustive search - just ignore the reversed version: ABCD has same cost as DCBA
def best(weights,n):
  min_cost = -1
  fact = lambda x: 1 if x==0 else x*fact(x-1)
  m1, m2 = 0, fact(n)
  for p in permutations(range(n)):
    c = 0
    for i in xrange(n-1):
      p1,p2 = p[i],p[i+1]
      c += weights[p1][p2]
    if c < min_cost or min_cost == -1:
      min_cost = c

    if m1 == m2:
      break
    m1 +=1
    m2 -=1

  return min_cost

def main():
  line = lambda : sys.stdin.readline().strip()

  n = int(line())
  weights = [[0]*n for i in xrange(n)]
  words = []
  for i in xrange(n):
    w = set(line())
    for k in xrange(len(words)):
      w2 = words[k]
      count = 0
      for ch in w2:
        if ch in w:
          count += 1
      weights[i][k] = count
      weights[k][i] = count
    words.append(w)

  print best(weights, n)

if __name__ == '__main__':
  main()
