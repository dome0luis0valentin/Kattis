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
  return (s_prev,t), s_prev*a+b*t

def main():
  print extended_gcd(int(sys.argv[1]), int(sys.argv[2]))

if __name__ == '__main__':
  main()
