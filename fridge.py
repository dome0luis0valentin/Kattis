import sys

def main():
  nums = sys.stdin.readline().strip()
  freq = [0 for i in xrange(10)]
  for i in nums:
    i = int(i)
    freq[i] += 1
  f = sorted(map(lambda x: (x[1],x[0]), enumerate(freq)))
  m = f[0]
  if m[1] != 0:
    print str(m[1])*(m[0]+1)
  else:
    m2 = f[1]
    if m[0] ==  m2[0] > 0:
      print str(m2[1])*(m2[0]+1)
    elif m[0] == m2[0] == 0:
      print m2[1]
    else:
      print "1"+"0"*(m[0]+1)

if __name__ == '__main__':
  main()
