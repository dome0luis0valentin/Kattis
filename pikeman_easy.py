import sys

def main():
  n,t = [int(i) for i in sys.stdin.readline().split()]
  A,B,C,t0 = [int(i) for i in sys.stdin.readline().split()]

  times = [t0]
  for i in xrange(n-1):
    times.append( ((A*times[-1] + B)%C)+1 )
  times.sort()
  penalty = 0
  curr_time = 0
  index = 0
  mod = 1000000007
  while (index < n):
    curr_time += times[index]
    if (curr_time > t):
      break
    penalty = (penalty+curr_time) % mod
    index += 1
  print index, penalty

if __name__ == '__main__':
  main()
