import sys

def main():
  line = lambda : sys.stdin.readline().strip()
  n,m = [int(i) for i in line().split()]
  while not(n == m == 0):
    heads = sorted([int(line()) for i in xrange(n)])
    knights = sorted([int(line()) for i in xrange(m)])

    k = 0
    price = 0
    for h in heads:
      while( k < m and h > knights[k]):
        k +=1
      if k >= m:
        price = -1
        break
      price += knights[k]
      k += 1

    if n > m or price == -1:
      print "Loowater is doomed!"
    else:
      print price

    n,m = [int(i) for i in line().split()]

if __name__ == '__main__':
  main()
