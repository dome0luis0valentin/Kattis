import sys

def main():
  n = int(sys.stdin.readline().strip())
  while True:
    original = [int(sys.stdin.readline().strip()) for i in xrange(n)]
    messed = [int(sys.stdin.readline().strip()) for i in xrange(n)]
    map_ = dict(zip(sorted(original), sorted(messed)))
    for i in original:
      print map_[i]
    n = int(sys.stdin.readline().strip())
    if n == 0:
      break
    print

if __name__ == '__main__':
  main()
