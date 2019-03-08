import sys

def process(start, useful, not_useful, garden, rows, cols):
  changes = [(0,1),(0,-1),(1,0),(-1,0)]
  visited = set()
  q = set([start])
  level = garden[start[0]][start[1]]
  while len(q) > 0:
    p = q.pop()
    visited.add(p)
    x,y = p
    for dx,dy in changes:
      xp,yp = x+dx, y+dy
      if 0<= xp <rows and 0<= yp <cols and (xp,yp) not in visited:
        if garden[xp][yp] < level:
          not_useful |= visited
          not_useful |= q
          return
        elif garden[xp][yp] == level:
          if (xp,yp) in not_useful:
            not_useful |= q
            not_useful |= visited
            return
          q.add((xp,yp))
        else:
          not_useful.add((xp,yp))

  useful |= visited

def solve(garden, rows, cols):
  not_useful = set()
  useful = set()
  for x in xrange(rows):
    for y in xrange(cols):
      if (x,y) not in useful and (x,y) not in not_useful:
        process((x,y), useful, not_useful, garden, rows, cols)
  return len(useful)

def main():
  line = lambda : sys.stdin.readline().strip()
  intList = lambda s: [int(k) for k in s.split()]
  cols, rows = [int(i) for i in line().split()]
  garden = []
  for i in xrange(rows):
    garden.append(intList(line().strip()))
  print solve(garden, rows, cols)

if __name__ == '__main__':
  main()
