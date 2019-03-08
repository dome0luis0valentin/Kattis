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
  return s_prev, t, s_prev*a + b*t

def main():
  sys.stdin.readline()
  for line in sys.stdin:
    R,S,Q = map(int, line.split())
    x,y,g = extended_gcd(R, S)
    k = Q/g
    x,y = x*k, y*k
    lcm = (R/g)*S
    dx, dy = lcm/R, lcm/S
    if x >= 0:
      k = x/dx - (1 if x%dx == 0 else 0)
      x,y = x - k*dx, y+k*dy
    else:
      k = abs(x)/dx + (1 if x%dx != 0 else 0)
      x,y = x+k*dx, y-k*dy

    if y <= 0:
      k = (y/dy) + 1
      x,y = x+k*dx, y-k*dy
    print x,y

if __name__ == '__main__':
  main()
