import sys

def f(b, i):
 p = i+1 # pratitions
 m = (-1*b) % p
 n = p - m
 a = (b + m)/p
 v1 = (a*a+a)/2
 v2 = v1 - a
 return m*v2 + n*v1

def main():
  line = lambda : sys.stdin.readline().strip()
  n, m, k = map(int, line().split())
  build = [0 for i in xrange(m+1)]
  for i in xrange(n):
    build[int(line())] += 1

  sum_to = lambda x: (x*x + x)/2
  prev = [0 for i in xrange(k+1)]
  for b in xrange(1,m+1):
    curr = [prev[0]+ sum_to(build[b])]
    # min noise if I had "b" buildings and allowed "j" emptyings
    for j in xrange(1,k+1):
      # figure out how many of the 'j' should be used on last building
      min_sofar = -1
      for i in xrange(j+1):
        noise = prev[j-i] + f(build[b], i)
        if min_sofar == -1 or noise < min_sofar:
          min_sofar = noise
      curr.append(min_sofar)
    prev = curr
  print prev[k]

if __name__ == '__main__':
  main()
