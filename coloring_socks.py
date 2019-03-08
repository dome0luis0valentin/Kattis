import sys

def main():
  line = lambda : sys.stdin.readline()
  s,c,max_diff = [int(k) for k in line().split()]
  colors = sorted([int(k) for k in line().split()])
  machines_tobuy = 1
  curr = 0
  start = colors[0]
  for i in colors:
    if curr == c:
      start = i
      machines_tobuy +=1
      curr = 0

    if i-start <= max_diff:
      curr +=1
    else:
      start = i
      machines_tobuy +=1
      curr = 1
  print machines_tobuy

if __name__ == '__main__':
  main()
