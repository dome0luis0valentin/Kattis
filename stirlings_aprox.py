import sys,math

def error_ratio(n):
  # compute the ration n!/s(n), where s(n) is stirling's approximation for n!
  numerator = 0
  for i in xrange(2,n):
    numerator += math.log(i)
  x = math.log(n)
  numerator += x
  denom = 0.5*math.log(2*math.pi) + (n+0.5)*x - n
  ratio = math.pow(math.e,numerator-denom)
  print "{:0.12f}".format(ratio)

def main():
  for line in sys.stdin:
    n = int(line.strip())
    if n==0:
      break
    error_ratio(n)

if __name__ == '__main__':
  main()
