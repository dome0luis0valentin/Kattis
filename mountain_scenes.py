import sys

M = 10**9 + 7
def all_scenes(n,w,h):
  prev = [min(i,h)+1 for i in xrange(n+1)] # for w=1
  prev_s = [1]
  for i in prev[1:]:
    prev_s.append(prev_s[-1]+i)

  nxt,nxt_s = [1],[1]
  for dw in xrange(2,w+1):
    for dn in xrange(1,n+1):
      # soln for f(dn,dw,h)
      if h >= dn:
        soln = prev_s[dn]
      else:
        soln = prev_s[dn]-prev_s[dn-h-1] % M
      nxt.append(soln)
      nxt_s.append(nxt_s[-1]+soln % M)
    prev,prev_s,nxt,nxt_s = nxt, nxt_s,[1],[1]

  return prev[-1]

def main():
  n,w,h = [int(i) for i in sys.stdin.readline().split()]
  count = all_scenes(n,w,h)
  identical = min(h, n/w) + 1
  count -=identical
  print count % M

if __name__ == '__main__':
  main()
