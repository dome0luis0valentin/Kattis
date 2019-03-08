import sys, math

def main():
  a,b,c,d = map(int, sys.stdin.readline().split())
  s = (a+b+c+d)/2.0
  print math.sqrt((s-a)*(s-b)*(s-c)*(s-d))

if __name__ == '__main__':
  main()
