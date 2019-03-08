import sys

def nth_rev(n):
  digits = "0125986"
  val = []
  while n:
    n,r = divmod(n,7)
    val.append(digits[r])
  print "".join(val)


def main():
  for line in sys.stdin:
    nth_rev(int(line.strip()))

if __name__ == "__main__":
  main()
