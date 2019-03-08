import sys

def convert(num, src, target):
  b1, b2 = len(src), len(target)
  src_map = dict([(src[i],i) for i in xrange(b1)])

  n = 0
  length = len(num)
  for i in xrange(length):
    n += src_map[num[length-i-1]]*(b1**i)

  n_b2 = []
  while n > 0:
    n,r = divmod(n,b2)
    n_b2.append(target[r])

  return "".join(reversed(n_b2))

def main():
  cases = int(sys.stdin.readline().strip())
  for c in xrange(cases):
    print "Case #{0}: {1}".format(c+1, convert(*sys.stdin.readline().split()))

if __name__ == '__main__':
  main()
