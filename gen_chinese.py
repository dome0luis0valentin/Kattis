import sys

def chinese_rem(a,n,b,m):
  s, s_prev = 0,1
  t, t_prev = 1,0
  r, r_prev = n,m

  while r != 0:
    q,rem = divmod(r_prev,r)
    r, r_prev = rem, r
    s, s_prev = s_prev - q*s, s

  t = (r_prev - s_prev*n) / m

  g = r_prev
  c1,c2 = s_prev,t
  if (a-b) % g != 0:
    return "no solution"

  p = (a-b)/g
  k = (n*m)/g
  x = (b + m*p*c1) % k
  return "{} {}".format(x,k)

def main():
  t = int(sys.stdin.readline().strip())
  for i in xrange(t):
    a,n,b,m = [int(i) for i in sys.stdin.readline().split()]
    print chinese_rem(a,n,b,m)
if __name__ == '__main__':
  main()
