import sys

def possible_moves(config, to_add, to_check, seen):
  changes = [(1,2),(2,1),(-1,2),(-2,1),(-1,-2),(-2,-1),(1,-2),(2,-1)]
  board = config[0]
  x,y = config[1]
  for dx,dy in changes:
    xp,yp = x+dx,y+dy
    if 0 <= xp < 5 and  0<= yp < 5:
      new_board = list(board)
      r1, r2 = new_board[x], new_board[xp]
      new_board[x] = r1[:y] + r2[yp] + r1[y+1:]
      new_board[xp] = r2[:yp] + " " + r2[yp+1:]
      conf = (tuple(new_board),(xp,yp))
      if conf in to_check:
        return True
      if conf not in seen:
        to_add.add(conf)
        seen.add(conf)
  return False

def solve(start, end):
  if start ==  end:
    return 0

  moves = 1
  seen_f, seen_b = set([start]), set([end])
  curr_f, curr_b = set([start]), set([end])
  while moves <= 10:
    if moves % 2: #forward
      forward = set()
      while len(curr_f) > 0:
        curr = curr_f.pop()
        if possible_moves(curr,forward, curr_b, seen_f):
          return moves
      curr_f = forward
    else: #backwards
      backward = set()
      while len(curr_b) > 0:
        curr = curr_b.pop()
        if possible_moves(curr,backward, curr_f, seen_b):
          return moves
      curr_b = backward
    moves +=1
  return -1

def main():
  line = lambda : sys.stdin.readline()
  n = int(line().strip())

  end=("11111","01111","00 11","00001","00000")
  # Get board config
  for k in xrange(n):
    start = [[],()]
    for i in xrange(5):
      row = line()[:5]
      if " " in row:
        start[1] = (i, row.index(" "))
      start[0].append(row)
    start[0] = tuple(start[0])
    moves = solve((start[0], start[1]),(end,(2,2)))

    if moves == -1:
      print "Unsolvable in less than 11 move(s)."
    else:
      print "Solvable in {} move(s).".format(moves)

if __name__ == '__main__':
  main()
