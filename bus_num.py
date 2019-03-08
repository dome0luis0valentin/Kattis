import sys

def main():
  getline = lambda : sys.stdin.readline().strip()
  n = int(getline())
  nums = [int(i) for i in getline().split()]
  nums.sort()
  reps = []
  i = 0
  while i < n:
    start = nums[i]
    end = start
    while i+1 < n and nums[i]+1 == nums[i+1]:
      i += 1
      end = nums[i]
    if end - start > 1:
      reps.append("{}-{}".format(start,end))
    elif end > start:
        reps.append(str(start))
        reps.append(str(end))
    else:
        reps.append(str(start))
    i += 1
  print " ".join(reps)

if __name__ == '__main__':
  main()
