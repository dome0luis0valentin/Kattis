import sys,math

def main():
  line = lambda : [int(k) for k in sys.stdin.readline().split()]
  n,m,k = line()
  avail_holes = sorted(line())
  circular = line()
  sqrt_2 = math.sqrt(2)
  square = map(lambda x: (sqrt_2*x)/2, line())
  houses = sorted(circular + square)
  hi, ai = 0,0
  c = 0
  while hi < len(houses) and ai < len(avail_holes):
    if houses[hi] < avail_holes[ai]:
      c += 1
      ai +=1
      hi += 1
    else:
      ai +=1
  print c

if __name__ == '__main__':
  main()
