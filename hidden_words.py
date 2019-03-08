import sys

def explore(board, start, words, h, w):
  x,y = start
  ch = board[x][y]
  q = [(start, set([start]), ch)]
  count = 0
  while len(q) > 0:
    p, seen, curr = q.pop()
    x,y = p
    if curr in words and words[curr] == 0: # seen for the first time
      words[curr] = 1
      count += 1
    if len(curr) == 10:
      continue
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
      xp,yp = x+dx, y+dy
      if 0 <= xp < h and 0<= yp < w and (xp,yp) not in seen:
        ch = board[xp][yp]
        new_curr = curr + ch
        new_seen = seen | set([(xp,yp)])
        q.append(((xp,yp), new_seen, new_curr))
  return count

def main():
  line = lambda : sys.stdin.readline().strip()
  h,w = map(int, line().split())
  board = [list(line()) for i in xrange(h)]
  word_c = int(line())
  words = {}
  for i in xrange(word_c):
    words[line()] = 0

  total = 0
  for x in xrange(h):
    for y in xrange(w):
      total += explore(board, (x,y), words, h, w)

  print total

if __name__ == '__main__':
  main()
