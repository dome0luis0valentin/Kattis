import sys, math

def main():
  for line in sys.stdin:
    p,q = [int(i) for i in line.split()]
    if (p == q == 0):
      break

    if (p==0): # Edge case
      print 0,2
    elif (p==q): # Edge case
      print 2,0
    else: # Normal case
      n = 2
      found_ans = False
      d = -1
      while ( n <= 50000 ):
        m = n*(n-1)
        if m%q == 0:
          k = m/q
          d = math.sqrt(1+4*k*p)
          if d == int(d) and int(d)%2 == 1:
            d = int(d)
            found_ans = True
            break
        n +=1
      if found_ans:
        r = (1+d)/2
        b = n - r
        print r,b
      else:
        print "impossible"

if __name__ == '__main__':
  main()
