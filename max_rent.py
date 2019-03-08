import sys

def main():
  a,b = [int(i) for i in sys.stdin.readline().split()]
  m,k = [int(i) for i in sys.stdin.readline().split()]
  p1 = (k - m, 2*m-k) # intesection of x+y = m & 2x+y=k
  p2, p3 = (1, k-2), (1,m-1)
  p4, p5 = (k/2,1), (m-1,1)

  rent = lambda x,y: a*x + b*y
  possible_vals = [p1,p2,p3,p4,p5]
  max_r = 0
  for p in possible_vals:
    x,y  = p
    if x>=1 and y>=1 and (x+y) <= m and 2*x+y >=k:
      v = rent(x,y)
      if v > max_r:
        max_r = v
  print max_r

if __name__ == '__main__':
  main()
