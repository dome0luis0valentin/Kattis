import sys

def main():
  for line in sys.stdin:
    nums = map(int,line.split())
    n, nums = nums[0], nums[1:]
    seen = set()
    is_jolly = True
    for i in xrange(n-1):
      diff = abs(nums[i] - nums[i+1])
      if diff in seen or diff >= n:
        is_jolly = False
        break
      seen.add(diff)
    print "Jolly" if is_jolly else "Not jolly"

if __name__ == '__main__':
  main()
