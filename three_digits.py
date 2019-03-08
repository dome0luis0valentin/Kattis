import sys

def last_3(n):
  fact = 1
  for i in xrange(2, n):
    fact = fact*i % 1000
    while fact%10 == 0:
      fact /= 10

  return str(fact)



def main():
  n = int(sys.stdin.readline().strip())
  ans = last_3(n)
  if len(ans) >= 3:
    print ans[-3:]
  else:
    print ans


if __name__ == '__main__':
  main()
