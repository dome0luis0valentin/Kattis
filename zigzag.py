import sys

def main():
  n = int(sys.stdin.readline().strip())
  count = 1
  last = int(sys.stdin.readline().strip())
  change = 0
  for i in xrange(n-1):
    num = int(sys.stdin.readline().strip())
    if last != num:
      new_change = num - last
      if change == 0 or new_change*change < 0:
        count += 1
        change = new_change
      last  = num
  print count

if __name__ == '__main__':
  main()
