import sys

def main():
  n = int(sys.stdin.readline().strip())
  for i in xrange(n):
    line,num = [int(i) for i in sys.stdin.readline().split()]
    s1 = num*(num+1)
    print line,s1/2,s1-num,s1

if __name__ == '__main__':
  main()
