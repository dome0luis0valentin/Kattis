import sys

def quickest_kill(h,t):
  base_cases = {(0,0): 0, (0,1):6, (1,1):3, (1,0):-1}

  moves = 0
  while (h,t) not in base_cases:
    if t >= 2:
      moves += t/2
      h,t = h+(t/2), t%2
    if h >= 2:
      moves += h/2
      h = (h%2)
  if base_cases[(h,t)] == -1:
    return -1
  return moves + base_cases[(h,t)]

def main():
  intList = lambda : [int(i) for i in sys.stdin.readline().split()]
  h,t = intList()
  while not (h == t == 0):
    m = [ quickest_kill(h,t) ]
    if t > 1:
      m2 = quickest_kill(h,t+1)
      if m2 > -1:
        m2 +=1
      m += [m2]
      m = [i for i in m if i != -1]
    if len(m) == 0:
      print -1
    else:
      print min(m)
    h,t = intList()

if __name__ == '__main__':
  main()
