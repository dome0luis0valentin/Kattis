import sys

def extended_gcd(a,b):
  s, s_prev = 0,1
  t, t_prev = 1,0
  r, r_prev = b,a

  while r != 0:
    q,rem = divmod(r_prev,r)
    r, r_prev = rem, r
    s, s_prev = s_prev - q*s, s

  t = (r_prev - s_prev*a) / b
  return (s_prev,t)

def inv(n,m):
  a,b = extended_gcd(n,m)
  return a%m

def generate(odds, a, b, M):
  print "\n".join(map(lambda x: str((a*x+b)%M), odds))

def main():
  getInt = lambda : int(sys.stdin.readline().strip())
  n = getInt()
  odds = [ getInt() for i in xrange(n)]
  M=10001
  untested_as = []
  poss_pair = []
  if n == 1:
    print odds[0]
    return
  for a in xrange(M-1):
    ap = a+1
    if ap % 73  != 0 and ap % 137 != 0:
      b = (odds[1] - a*a*odds[0])*inv(ap,M)
      if n == 2:
        generate(odds,a,b,M)
        break
      elif (a*a*odds[1] + a*b + b) % M == odds[2]:
        generate(odds,a,b,M)
        break


if __name__ == '__main__':
  main()
