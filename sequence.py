import sys

MAX_INT = 1000000001 # all int elems given are less than or eq 10**9

def solve(nums,nxt_p,prev_p,n):
  cost,reduces = 0,0
  i = 1
  while (reduces < n-1):
    if i == 0:
      i = nxt_p[i]
      continue
    pi, ni = prev_p[i], nxt_p[i]
    prev, curr, nxt = nums[pi], nums[i], nums[ni]
    if prev >= curr <= nxt:
      nxt_p[pi] = ni
      prev_p[ni] = pi
      i = pi
      cost += min(prev, nxt)
      reduces += 1
    else:
      i = ni
  return cost

def main():
  n = int(sys.stdin.readline().strip())
  nums = [MAX_INT]
  nxt,prev = [1],[-1]
  for i in sys.stdin:
    nums.append(int(i.strip()))
    nxt.append(nxt[-1]+1)
    prev.append(prev[-1]+1)
  nums.append(MAX_INT)
  nxt.append(n+1)
  prev.append(n)
  print solve(nums,nxt,prev,n)

if __name__ == '__main__':
  main()
