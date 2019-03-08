import sys

def gcd(x,y):
  while(y):
    x,y = y,x%y
  return x

def gcds(nums):
  all_gcds = set(nums)
  lvl_gcds = []
  while(len(nums) > 1):
    for i in xrange(1,len(nums)):
      new_gcd = gcd(nums[i-1],nums[i])
      if len(lvl_gcds) == 0 or lvl_gcds[-1] != new_gcd:
        lvl_gcds.append(new_gcd)
        all_gcds.add(new_gcd)
    nums,lvl_gcds = lvl_gcds,[]
  return len(all_gcds)

def main():
  n = int(sys.stdin.readline().strip())
  nums = []
  for i in xrange(n):
    nums.append(int(sys.stdin.readline().strip()))
  print gcds(nums)

if __name__ == "__main__":
  main()
