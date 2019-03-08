import sys

def main():
  n = int(sys.stdin.readline().strip())
  nums = []
  for line in sys.stdin:
    a,b = [int(i) for i in line.split()]
    nums.append((a,b))

    
