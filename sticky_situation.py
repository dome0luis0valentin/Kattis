import sys

def main():
  line = lambda :sys.stdin.readline().strip()
  n = int(line())
  nums = sorted([int(i) for i in line().split()])
  for i in xrange(n-2):
    if nums[i] + nums[i+1] > nums[i+2]:
      print "possible"
      return
  print "impossible"

if __name__ == '__main__':
  main()

