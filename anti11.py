import sys
M = (10**9) + 7
def anti11(n):
  ends_in0, ends_in1 = 1,1
  for i in xrange(2,n+1):
    ends_in0, ends_in1 = (ends_in0 + ends_in1) % M, ends_in0 % M
  return (ends_in0 + ends_in1) % M

def main():
  getInt = lambda : int(sys.stdin.readline().strip())
  t = getInt()
  for i in xrange(t):
    print anti11(getInt())

if __name__ == '__main__':
  main()
