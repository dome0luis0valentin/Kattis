import sys

def fill(board, covered, n):
  changes = 0
  for cx, cy in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
    if (cx, cy) in covered[n][2]:
      continue
    cx, cy = cx*3, cy*3
    allowed_rows = [i for i in xrange(cx, cx+3) if i not in covered[n][0]]
    allowed_cols = [i for i in xrange(cy, cy+3) if i not in covered[n][1]]
    possible = []
    for x in allowed_rows:
      for y in allowed_cols:
        if board[x][y] == ".":
          possible.append((x,y))

    if len(possible) == 0:
      return -1
    elif len(possible) == 1:
      x,y = possible[0]
      changes +=1
      board[x][y] = n
      covered[n][0].add(x)
      covered[n][1].add(y)
      covered[n][2].add((cx/3, cy/3))

  return changes

def cross_hatching(board, covered):
  delta = 1
  while delta > 0:
    delta = 0
    for i in "123456789":
      c = fill(board, covered, i)
      if c == -1:
        return -1
      delta += c
  return delta

def main():
  board = []
  # val -> set of: covered rows, covered cols, covered boxes
  covered = dict(map(lambda x: (x,[set(),set(),set()]),list("123456789")))
  row = 0
  for line in sys.stdin:
    board.append(list(line.strip()))
    for col in xrange(9):
      if line[col] != ".":
        cover = covered[line[col]]
        box = (row/3, col/3)
        if row in cover[0] or col in cover[1] or box in cover[2]:
          print "ERROR"
          return
        else:
          cover[0].add(row)
          cover[1].add(col)
          cover[2].add(box)
    row +=1
  if cross_hatching(board, covered) == -1:
    print "ERROR"
  else:
    print "\n".join(map(lambda x: "".join(x), board))

if __name__ == '__main__':
  main()
