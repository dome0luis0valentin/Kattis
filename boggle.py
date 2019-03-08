import sys

def all_from(board, start, words, found):
  x,y = start
  ch = board[x][y]
  q = [(start, set([start]), ch)]
  while len(q) > 0:
    p, seen, curr = q.pop()
    x,y = p
    if curr in words:
      found.add(curr)
    if len(curr) == 8:
      continue
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]:
      xp, yp = x+dx, y+dy
      if 0<= xp < 4 and 0<= yp < 4 and (xp,yp) not in seen:
        ch = board[xp][yp]
        new_curr = curr + ch
        new_seen = seen | set([(xp,yp)])
        q.append(((xp,yp), new_seen, new_curr))

ans_key = {}
def solve(board, words):
  b = "".join(board)
  if b in ans_key:
    return ans_key[b]
  found = set()
  for x in xrange(4):
    for y in xrange(4):
      all_from(board, (x,y), words, found)

  score = 0
  sm = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}
  lw, word = 0, ""
  for w in found:
    curr_l = len(w)
    if curr_l > lw or (lw == curr_l and word > w):
      lw, word =  curr_l, w
    score += sm[curr_l]
  ans_key[b] = (score, word, len(found))
  return score, word, len(found)


def main():
  line = lambda : sys.stdin.readline().strip()
  w = int(line())
  words = set()
  for i in xrange(w):
    words.add(line())
  line()

  t = int(line())
  for j in xrange(t):
    board = [line() for i in xrange(4)]
    line()
    s,w,f = solve(board, words)
    print s,w,f

if __name__ == '__main__':
  main()
