import sys

def main():
  n = int(sys.stdin.readline().strip())
  prices = []
  for line in sys.stdin:
    prices.append(int(line.strip()))
  prices.sort(reverse=True)
  min_price = 0
  for i in xrange(n):
    if i%3 != 2:
      min_price += prices[i]
  print min_price

if __name__ == '__main__':
  main()
