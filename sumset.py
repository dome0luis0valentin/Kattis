import sys
from itertools import combinations

def main():
  nums = []
  n = int(sys.stdin.readline().strip())
  for line in sys.stdin:
    nums.append(int(line.strip()))

  MAX, MIN = max(nums), min(nums)

  sum_map = {}
  for i,j in combinations(xrange(n),2):
    s = nums[i] + nums[j]
    sum_map[s] = (i,j)

  max_sofar = MIN-1
  for i,j in combinations(xrange(n),2):
    d1 = nums[i] - nums[j]
    if d1 in sum_map:
      p,q = sum_map[d1]
      if i!=p and i!=q and j!=p and j!=q:
        if max_sofar < nums[i]:
          max_sofar = nums[i]

    d2 = nums[j] - nums[i]
    if d2 in sum_map:
      p,q = sum_map[d2]
      if i!=p and i!=q and j!=p and j!=q:
        if max_sofar < nums[j]:
          max_sofar = nums[j]
    if max_sofar == MAX:
      break
  print max_sofar if max_sofar != (MIN-1) else "no solution"

if __name__ == '__main__':
  main()
