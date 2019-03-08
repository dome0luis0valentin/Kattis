import sys

def main():
  n = int(sys.stdin.readline().strip())
  q,r = divmod(n,8)
  if r == 5 or r == 0:
    print n
  elif r>5:
    print 8*(q+1)
  else:
    print q*8 + 5

if __name__ == '__main__':
  main()
