import sys

M = 1000

def mult(a,b):
  return [(a[0]*b[0]+a[1]*b[2]) % M, (a[0]*b[1] + a[1]*b[3]) % M,
          (a[2]*b[0]+a[3]*b[2]) % M, (a[2]*b[1] + a[3]*b[3]) % M]

def matrix_expo(a,n):
  if n == 1:
    return a
  if n%2 == 0:
    half_way = matrix_expo(a , n/2)
    return mult(half_way, half_way)
  return mult(a, matrix_expo(a, n-1))

def main():
  cases = int(sys.stdin.readline().strip())
  for i in xrange(1, cases+1):
    n = int(sys.stdin.readline().strip())
    a_n = matrix_expo([3,5,1,3],n)
    ans = (2*a_n[0] - 1) % M
    print "Case #{}: {:03d}".format(i,ans)

if __name__ == '__main__':
  main()
