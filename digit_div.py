import sys

MOD = (10**9) + 7
def parts(list_num, n, m):
  curr  = 0
  count = 0
  for i in xrange(1,n+1):
    d = list_num.pop()
    curr = curr*10 + int(d)
    if curr % m == 0:
      count += 1
      curr = 0
  if curr % m == 0:
    return count
  return 0



def main():
  line = lambda : sys.stdin.readline().strip()
  n,m = map(int, line().split())
  list_num = list(reversed(line()))
  p = parts(list_num, n, m)
  if p == 0:
    print 0
  else:
    print pow(2, p-1, MOD)

if __name__ == '__main__':
  main()
