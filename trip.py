import sys

def main():
  n = int(sys.stdin.readline().strip())
  while (n > 0):
    payments = []
    total = 0
    for i in xrange(n):
      p = int(round(float(sys.stdin.readline().strip())*100))
      payments.append(p)
      total += p
    avg = total/n
    remain = total%n

    min_transfer = 0
    more_than_avg = 0
    for p in payments:
      if p>avg:
        min_transfer += (p-avg)
        more_than_avg +=1
    min_transfer -= min(remain,more_than_avg)
    print "$%0.2f" % (min_transfer/100.0)
    n = int(sys.stdin.readline().strip())


if __name__ == '__main__':
  main()
