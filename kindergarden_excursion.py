import sys

def main():
  order = sys.stdin.readline().strip()
  ones, twos = 0,0
  total = 0
  for i in order:
    if i == '0':
      total += (ones + twos)
    elif i == '1':
      total += twos
      ones +=1
    else:
      twos +=1
  print total

if __name__ == '__main__':
  main()
