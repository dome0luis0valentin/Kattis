import sys

def main():
  line = lambda : sys.stdin.readline()
  n,m = map(int, line().split())
  weights = sorted(map(int, line().split()), reverse=True)
  getInts = lambda : [int(i) for i in line().split()]
  buyers = [ getInts() for k in xrange(m) ]
  buyers.sort(key=lambda x:x[1], reverse=True)

  i,j = 0,0
  total = 0
  while i<n and j<m:
    curr_w = weights[i]
    need, price = buyers[j]
    total += curr_w*price
    need -= 1
    if need == 0:
      j +=1
    else:
      buyers[j][0] -= 1
    i+=1
  print total

if __name__ == '__main__':
  main()
