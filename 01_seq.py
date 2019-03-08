import sys

def main():
  line = sys.stdin.readline().strip()
  inversions,count,zeros = 0,1,0
  for ch in reversed(line):
    if ch == "0":
      zeros += count
    elif ch == "1":
      inversions += zeros
    else:
      inversions += inversions+zeros
      zeros += zeros + count
      count += count
    inversions = inversions % 1000000007
    zeros = zeros % 1000000007
    count = count % 1000000007
  print inversions 

if __name__ == "__main__":
  main()

