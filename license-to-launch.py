import sys

def main():
  sys.stdin.readline()
  nums = sys.stdin.readline().split()
  min_sofar, d = 1000000001, 0
  for i,v in enumerate(nums):
   v = int(v)
   if v < min_sofar:
     min_sofar = v
     d = i
  print d

if __name__ == '__main__':
  main()
