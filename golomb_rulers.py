import sys

def determin(nums):
  nums.sort()
  seen = set()
  max_v = 0
  for i in xrange(len(nums)):
    if nums[i] > max_v:
      max_v = nums[i]
    for j in xrange(i+1,len(nums)):
      v = nums[j] - nums[i]
      if v in seen:
        return "not a ruler"
      else:
        seen.add(v)
  if len(seen) == max_v:
    return "perfect"
  else:
    return "missing {}".format(" ".join([str(k) for k in xrange(1,max_v+1) if k not in seen]))

def main():
  for line in sys.stdin:
    print determin([int(k) for k in line.split()])

if __name__ == '__main__':
  main()
