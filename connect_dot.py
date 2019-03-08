import sys

ch_val = dict(zip(list("0123456789")+map(chr, range(97,97+26)+range(65,65+26)),
                  range(10+26*2)))

def connect(board, start, end):
  dx = start[0] - end[0]
  if dx == 0:
    x = start[0]
    y1,y2 = min(start[1], end[1])+1, max(start[1], end[1])
    for i in xrange(y1, y2):
      if board[x][i] == "|":
        board[x][i] = "+"
      elif board[x][i] == ".":
        board[x][i] = "-"
  else:
    y = start[1]
    x1,x2 = min(start[0], end[0])+1, max(start[0], end[0])
    for i in xrange(x1, x2):
      if board[i][y] == "-":
        board[i][y] = "+"
      elif board[i][y] == ".":
        board[i][y] = "|"


def process(board,positions):
  to_connect = sorted(positions.keys(), key=lambda x: ch_val[x])
  for i in xrange(len(to_connect)-1):
   start, end = to_connect[i], to_connect[i+1]
   connect(board, positions[start], positions[end])
  print "\n".join(map(lambda x: "".join(x), board))

def main():
  board = []
  positions = {}
  row, col = 0,0
  for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
      process(board,positions)
      print
      board, positions = [], {}
      row,col = 0,0
    else:
      list_line = []
      col = 0
      for ch in line:
        list_line.append(ch)
        if ch != ".":
          positions[ch] = (row,col)
        col +=1
      board.append(list_line)
      row +=1
  process(board,positions)

if __name__ == '__main__':
  main()

