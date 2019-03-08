import sys

def div_print(x,y,n):
  digits = []
  big = str(x/y)
  x = (x%y)*10
  for i in xrange(n):
    digits.append(str(x/y))
    x = (x%y)*10
    if x == 0:
      break
  print big+"."+"".join(digits).ljust(n,"0")

def main():
  for line in sys.stdin:
    div_print(*[int(i) for i in line.strip().split()])

if __name__ == '__main__':
  main()
