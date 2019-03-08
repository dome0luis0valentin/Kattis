import sys
import bisect

def main():
  n, m = map(int, sys.stdin.readline().split())
  nums = [int(i) for i in sys.stdin.readline().split()]
  nums.sort()
  prefix = [0]
  for i in nums:
    prefix.append(prefix[-1]+i)

  # binary search
  low, high = 0, nums[-1]
  last = 0
  while low < high-1:
    mid = (low + high)/2
    last_uncut = bisect.bisect_right(nums, mid)
    collected = (prefix[-1] - prefix[last_uncut]) - ((n-last_uncut)*mid)
    if collected == m:
      break
    elif collected > m:
      low = mid
    elif collected < m:
      high = mid

  if high - low == 1:
    print low
  else:
    print low+high/2

if __name__ == '__main__':
  main()
