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
  while True:
    n,t = [int(i) for i in sys.stdin.readline().split()]
    if n == t == 0:
      break
    for i in xrange(t):
      a,op,b = sys.stdin.readline().split()
      a,b = int(a), int(b)
      if op == "+":
        print (a + b) % n
      elif op == "-":
        print (a - b) % n
      elif op == "*":
        print (a * b) % n
      else:
        x,y = extended_gcd(b,n)
        if x*b + y*n == 1:
          print (x*a) % n
        else:
          print -1

if __name__ == '__main__':
  main()
