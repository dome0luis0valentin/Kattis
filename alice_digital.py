import sys

def main():
  t = int(sys.stdin.readline().strip())
  for j in xrange(t):
    n,m = [int(k) for k in sys.stdin.readline().split()]
    nums = [int(x) for x in sys.stdin.readline().split()]
    max_sofar = 0
    for i in xrange(n):
      if nums[i] == m:
        total = m
        for k in xrange(i-1, -1,-1):
          if nums[k] <= m:
            break
          total += nums[k]
        for k in xrange(i+1, n):
          if nums[k] <= m:
            break
          total += nums[k]
        if total > max_sofar:
          max_sofar = total
        
    print max_sofar

if __name__ == '__main__':
  main()


        


