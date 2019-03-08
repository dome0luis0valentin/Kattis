import sys

def main():
  t = int(sys.stdin.readline().strip())
  for line in sys.stdin:
    l,r = [int(i) for i in line.split()]
    print ((l*l+l)/2)+ 1 + (l*r + r) + ((r*r+r)/2)

if __name__ == '__main__':
  main()
