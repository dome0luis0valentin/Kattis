import sys

def main():
  case = int(sys.stdin.readline().strip())
  for i in xrange(case):
    n = int(sys.stdin.readline().strip())
    nums = [int(k) for k in sys.stdin.readline().split()]
    curr = 0
    for j in nums:
      if j == curr+1:
        curr += 1
    print n - curr

if __name__ == '__main__':
  main()
