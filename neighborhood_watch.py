import sys

def main():
  line = lambda : sys.stdin.readline().strip()
  n, k = map(int, line().split())
  safe_paths = (n*n+n)/2
  prev = 0
  for i in xrange(k):
    curr = int(line())
    diff = (curr - prev - 1)
    safe_paths -= (diff*diff + diff)/2
    prev = curr
  last_diff = n-prev
  safe_paths -= (last_diff*(last_diff +1 ))/2
  print safe_paths

if __name__ == '__main__':
  main()
