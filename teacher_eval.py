import sys,math

def main():
  getInts = lambda : [int(i) for i in sys.stdin.readline().split()]
  n, p = getInts()
  if p == 100:
    print "impossible"
    return
  curr_sum = sum(getInts())
  diff = p*n - curr_sum
  print int(math.ceil((diff*1.0)/(100-p)))

if __name__ == '__main__':
  main()
