import sys
from collections import defaultdict

def solve(board, start, rows, cols):
  curr, nxt = [(start,'-',0)], []
  steps = 0
  seen = set()
  while len(curr) + len(nxt) > 0:
    if len(curr) == 0:
      steps += 1
      curr, nxt = nxt, curr

    at, direc, count = curr.pop()
    x,y = at
    if board[x][y] == "D":
      return steps
    seen.add((at, direc, count))
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
      xp, yp = x+dx, y+dy
      if not(0<= xp < rows and 0<= yp <cols):
        continue
      if (dx,dy) == (0,1) and direc != "left": # move right
        p, d = (xp,yp), "right"
        new_c = count + 1 if "right" == direc else 1
        new_e = (p,d,new_c)
        if new_c <= 2 and new_e not in seen and board[xp][yp] != "B":
          nxt.append(new_e)
      elif (dx,dy) == (0,-1) and direc != "right": # move left
        p, d = (xp,yp), "left"
        new_c = count + 1 if "left" == direc else 1
        new_e = (p,d,new_c)
        if new_c <= 2 and new_e not in seen and board[xp][yp] != "B":
          nxt.append(new_e)
      elif (dx,dy) == (-1,0) and direc != "down": # move up
        p, d = (xp,yp), "up"
        new_c = count + 1 if "up" == direc else 1
        new_e = (p,d,new_c)
        if new_c <= 2 and new_e not in seen and board[xp][yp] != "B":
          nxt.append(new_e)
      elif (dx,dy) == (1,0) and direc != "up": # move down
        p, d = (xp,yp), "down"
        new_c = count + 1 if "down" == direc else 1
        new_e = (p,d,new_c)
        if new_c <= 2 and new_e not in seen and board[xp][yp] != "B":
          nxt.append(new_e)
  return -1

def main():
  line = lambda : sys.stdin.readline().strip()
  n = int(line())
  for i in xrange(n):
    line()
    rows, cols = map(int, line().split())
    board = []
    start, dest = (0,0), (0,0)
    for r in xrange(rows):
      row = line()
      for c,ch in enumerate(row):
        if ch == "R":
          start = (r,c)
      board.append(row)

    print solve(board, start, rows, cols)

if __name__ == '__main__':
  main()
