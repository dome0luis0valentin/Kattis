import sys,math

def main():
  n = int(sys.stdin.readline().strip())
  m = int(math.pow(n, 1.0/9))+1
  meow_fact = 1
  for i in xrange(2,m+1):
    if (n % i**9) == 0:
      meow_fact = i
  print meow_fact

if __name__ == '__main__':
  main()
