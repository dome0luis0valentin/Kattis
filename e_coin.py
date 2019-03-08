import sys, math
from collections import defaultdict

def triples(n):
  tri = defaultdict(list)
  for x in range(0, n+1):
    for y in range(0, n+1):
      z_sq = x**2 + y**2
      z = int(math.sqrt(z_sq))
      if z**2 == z_sq:
        tri[z].append((x,y))
  return tri

def min_coins(denominations,n):
  table = [ [-1]*(n+1) for k in range(n+1)]
  table[0][0] = 0
  for x in range(n+1):
    for y in range(n+1):
      if table[x][y] != -1:
        continue
      min_sofar = -1
      for dx,dy in denominations:
        xp,yp = x-dx, y-dy
        if xp >= 0 and yp >= 0:
          if table[xp][yp] >= 0 and (min_sofar==-1 or table[xp][yp]<min_sofar):
            min_sofar = 1+table[xp][yp]
      table[x][y] = min_sofar
  return table

def bfs(denominations, start):
  curr_f, nxt_f = [start], []
  curr_b, nxt_b = [(0,0)], []
  step_f, step_b = 0,0
  max_x, max_y = start
  mod = max_x**2 + max_y**2
  seen_f = [[False]*(max_y+1) for i in xrange(max_x+1)]
  seen_b = [[False]*(max_y+1) for i in xrange(max_x+1)]
  while len(curr_f)+len(curr_b) > 0:
    #print len(curr_f), len(curr_b)
    # Forward direction
    while len(curr_f) > 0:
      x,y = curr_f.pop()
      seen_f[x][y] = True
      if seen_b[x][y]:
        return step_f + step_b
      for dx, dy in denominations:
        xp, yp = x-dx, y-dy
        if xp>=0 and yp >=0:
          if not seen_f[xp][yp]:
            seen_f[xp][yp] = True
            nxt_f.append((xp,yp))
    curr_f, nxt_f = nxt_f, curr_f
    if len(curr_f) > 0:
      step_f +=1

    # backward direction
    while len(curr_b) > 0:
      x,y = curr_b.pop()
      seen_b[x][y] = True
      if seen_f[x][y]:
        return step_f+step_b
      for dx, dy in denominations:
        xp, yp = x+dx, y+dy
        if (xp**2 + yp**2 <= mod) and (xp <= max_x and yp <= max_y):
          if not seen_b[xp][yp]:
            seen_b[xp][yp] = True
            nxt_b.append((xp,yp))
    curr_b, nxt_b = nxt_b, curr_b
    if len(curr_b) > 0:
      step_b +=1

  return -1

t = triples(300)
def solve(denominations, s):
  min_sofar = -1
  for x,y in t[s]:
    v = bfs(denominations, (x,y))
    if v != -1:
      if v < min_sofar or min_sofar == -1:
        min_sofar = v
  print "not possible" if min_sofar == -1 else min_sofar


def main():
  cases = int(sys.stdin.readline().strip())

  getFirst = True
  denominations = []
  for line in sys.stdin:
    line = line.strip()
    if line == "":
      getFirst = True
      solve(denominations, s)
      continue

    if getFirst:
      m,s = [int(k) for k in line.split()]
      denominations = []
      getFirst = False
    else:
      denominations.append([int(k) for k in line.split()])

  solve(denominations, s)

if __name__ == '__main__':
  main()

