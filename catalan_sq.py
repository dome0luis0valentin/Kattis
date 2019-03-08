import sys,time

def comb(n,m):
  small = min(m, n-m)
  
  ans = 1
  for i in xrange(1,small+1):
    ans *= n
    ans /= i
    n -=1
  return ans

def catal_sq(n):
  ans = comb(2*n,n)/(n+1) 
  return ans
  
def main():
  #print comb( int(sys.argv[1]), int(sys.argv[2]) )
  print catal_sq(int(sys.stdin.readline().strip())+1)

if __name__ == '__main__':
  main()
