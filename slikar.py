import sys

def flood(board, waters, rows, cols):
  flood_time = dict(zip(waters,[0]*len(waters)))
  time = 1
  while len(waters) > 0:
    new_waters = set()
    for x,y in waters:
      for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        xp, yp = x+dx, y+dy
        if 0<=xp<rows and 0<=yp<cols:
          if board[xp][yp] in ".S" and (xp,yp) not in flood_time:
            new_waters.add((xp,yp))
            flood_time[(xp,yp)] = time
    time += 1
    waters = new_waters
  return flood_time

def solve(board, start, rows, cols, seen, waters):
  flood_time = flood(board, waters, rows, cols)
  q = set([start])
  time = 0
  while (len(q) > 0):
    nxt_q = set()
    for x,y in q:
      if board[x][y] == "D":
        return time
      seen[x*cols+y] = True
      for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        xp, yp = x+dx, y+dy
        if 0<= xp <rows and 0<= yp <cols:
          if not seen[xp*cols+yp] and ((xp,yp) not in flood_time or
            flood_time[(xp,yp)] > time+1) and board[xp][yp] != "X":
            nxt_q.add((xp,yp))
    time += 1
    q = nxt_q
  return -1

def main():
  line = lambda : sys.stdin.readline().strip()
  rows, cols = map(int, line().split())
  board = []
  start = (0,0)
  waters = set()
  for r in xrange(rows):
    l = list(line())
    board.append(l)
    for c in xrange(cols):
      if l[c] == "S":
        start = (r,c)
      elif l[c] == "*":
        waters.add((r,c))
  seen = [False for i in xrange(rows*cols)]
  t = solve(board, start, rows, cols, seen, waters)
  print t if t > -1 else "KAKTUS"

if __name__ == '__main__':
  main()
