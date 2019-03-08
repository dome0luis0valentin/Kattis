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

def main():
  t = int(sys.stdin.readline().strip())
  for i in xrange(t):
    a,n,b,m = [int(i) for i in sys.stdin.readline().split()]
    bezot_c = extended_gcd(n,m)
    k = n*m
    x = (a*bezot_c[1]*m + b*bezot_c[0]*n) % k
    print x,k

if __name__ == '__main__':
  main()
