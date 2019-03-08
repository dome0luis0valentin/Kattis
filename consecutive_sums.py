import sys,math

def consec_sums(n):
  sq = int(math.sqrt(2*n))+1
  a,k = 0,0
  for p in xrange(2,sq):
    val = 2*n - p*p +p
    if val % (2*p) == 0:
      a = val/(2*p)
      k = p
      break
  if a == k == 0:
    return "IMPOSSIBLE"
  else:
    str_sum = " + ".join([str(a+i) for i in xrange(k)])
    return "{0} = {1}".format(n,str_sum)


def main():
  n = sys.stdin.readline()
  for line in sys.stdin:
    print consec_sums(int(line.strip()))

if __name__ == "__main__":
  main()

