import sys

def positions(board, word, size):
  letter_pos = dict([(i,set()) for i in set(list(word))])
  for n,w in enumerate(board):
    x,y = n/size, n%size
    if w in letter_pos:
      letter_pos[w].add((x,y))
  return letter_pos

def find(pos, s, w, ends_at) :
  q = [(s, 1)]
  while len(q) > 0:
    p, at = q.pop()
    if at == len(w):
      ends_at.add(p)
      continue
    ch = w[at]
    cx, cy = p
    for dx,dy in [(1,2),(2,1),(-1,-2),(-2,-1),(-1,2),(2,-1),(1,-2),(-2,1)]:
      x, y = cx+dx, cy+dy
      if (x,y) in pos[ch]:
        q.append(((x,y),at+1))

def knight_search(board, word, size):
  pos = positions(board, word, size)
  if reduce(lambda x,y: x*y, map(len, pos.values())) == 0:
    return False

  first_half = word[:len(word)/2]
  second_half = "".join(reversed(word[len(word)/2:]))
  set1, set2 = set(), set()
  for p in pos[first_half[0]]:
    find(pos, p, first_half, set1)

  if len(set1) == 0:
    return False
  for p in pos[second_half[0]]:
    find(pos, p, second_half, set2)
  if len(set2) == 0:
    return False

  if len(set1) > len(set2):
    set1, set2 = set2, set1

  for p in set1:
    x,y = p
    for dx,dy in [(1,2),(2,1),(-1,-2),(-2,-1),(-1,2),(2,-1),(1,-2),(-2,1)]:
      xp, yp = x+dx, y+dy
      if (xp,yp) in set2:
        return True
  return False

def main():
  n = int(sys.stdin.readline().strip())
  board = sys.stdin.readline().strip()

  if knight_search(board, "ICPCASIASG", n):
    print "YES"
  else:
    print "NO"

if __name__ == '__main__':
  main()
