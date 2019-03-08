import sys,math

def main():
  n,k,q = [float(i) for i in sys.stdin.readline().split()]
  for line in sys.stdin:
    x,y = [int(i) for i in line.split()]
    steps = 0
    x,y = (x-1,y-1) if x < y else (y-1,x-1)
    while(x!=y):
      y = math.ceil(y/k) - 1
      x,y = (x,y) if x < y else (y,x)
      steps +=1
    print steps

if __name__ == '__main__':
  main()
