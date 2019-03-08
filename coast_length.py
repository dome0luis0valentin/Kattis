import sys

def coast_length(board, cols, rows):
  q = [(0,0)]
  seen = set()
  coast_len = 0
  while len(q) > 0:
    x,y = q.pop()
    if (x,y) not in seen:
      seen.add((x,y))
      for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        xp, yp = x+dx, y+dy
        if 0 <= xp < rows and 0 <= yp < cols:
          if board[xp][yp] == "0":
            q.append((xp,yp))
          else:
            coast_len += 1
  return coast_len

def main():
  getLine = lambda : sys.stdin.readline().strip()
  rows, cols = [int(i)+2 for i in getLine().split()]
  board = [["0"]*(cols)]
  for r in xrange(1,rows-1):
    row = list("0{}0".format(getLine()))
    board.append(row)
  board.append(["0"]*cols)
  print coast_length(board, cols, rows)

if __name__ == '__main__':
  main()
