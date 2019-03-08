import sys

def main():
  case = int(sys.stdin.readline().strip())
  for i in xrange(case):
    k,n = [int(i) for i in sys.stdin.readline().split()]
    nums = []
    while len(nums) < n:
      nums += [int(i) for i in sys.stdin.readline().split()]
    sorted_nums = sorted(nums)
    da = 0
    index = 0
    for j in nums:
      if j != sorted_nums[index]:
        da += 1
      else:
        index +=1
    print "{0} {1}".format(k,da)

if __name__ == '__main__':
  main()

