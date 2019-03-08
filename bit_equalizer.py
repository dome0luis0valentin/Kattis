import sys

def main():
  cases = int(sys.stdin.readline().strip())
  for i in xrange(cases):
    src = sys.stdin.readline().strip()
    target = sys.stdin.readline().strip()
    print "Case {0}: {1}".format(i+1, mutate(src,target))

if __name__ == '__main__':
  main()
