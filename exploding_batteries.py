import sys, math

def main():
  f = lambda k: int(math.ceil((math.sqrt(1+8*k) - 1)/2))
  for line in sys.stdin:
    n = int(line.strip())
    if n==0:
      break
    print f(n-1)

if __name__ == '__main__':
  main()
