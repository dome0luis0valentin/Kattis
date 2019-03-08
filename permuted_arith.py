import sys

def determine(nums):
  nums2 = sorted(nums)
  diff = nums2[0] - nums2[1]
  for i in xrange(1,len(nums2)):
    if diff != (nums2[i-1] - nums2[i]):
      return "non-arithmetic"
  if sum(map(lambda x: abs(x[0]-x[1]), zip(nums2,nums))) == 0:
    return "arithmetic"
  return "permuted arithmetic"

def main():
  sys.stdin.readline()
  for line in sys.stdin:
    nums = [int(k) for k in line.split()][1:]
    print determine(nums)

if __name__ == '__main__':
  main()
