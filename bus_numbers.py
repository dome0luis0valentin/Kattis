import sys, math

cube_root = lambda x : int(math.ceil(x**(1.0/3.0)))

def check(n):
  lim = cube_root(n)
  count = 0
  already_used = set()
  for a in xrange(1,lim+1):
    a_cube = a**3
    b = n - a_cube
    if b>0 and (b not in already_used) and b == cube_root(b)**3:
      already_used.add(a_cube)
      count +=1
    if count == 2:
      return True
  return False

def main():
  n = int(sys.stdin.readline().strip())
  for i in xrange(n,1728,-1):
    if check(i):
      print i
      return
  print "none"

if __name__ == '__main__':
  main()
