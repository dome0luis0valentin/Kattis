import sys

def main():
  n = int(sys.stdin.readline().strip())
  y = n-1
  pos = []
  for i in xrange(n):
    line = sys.stdin.readline().strip()
    for x in xrange(n):
      if line[x] == '.':
        pos.append((x,y))
    y -=1
  cipher_text = sys.stdin.readline().strip()
  grid = [[" "]*n for i in xrange(n)]
  curr = sorted(pos, key = lambda x:10**x[1] + (n-x[0]), reverse=True)
  covered = set(curr)
  # No secrets if grill is only holes
  if len(covered) == n*n:
    print "invalid grille"
    return
  cut = len(pos)
  for rot in xrange(4):
    pos = set()
    cipher_p = cipher_text[rot*cut:(rot+1)*cut]
    for (x,y),ch in zip(curr,cipher_p):
      new_x, new_y = y,n-x-1
      pos.add((new_x,new_y))
      covered.add((new_x,new_y))
      grid[y][x] = ch
    curr = sorted(pos, key = lambda x:10**x[1] + (n-x[0]), reverse=True)

  if len(covered) != n*n:
    print "invalid grille"
  else:
    g = ["".join(i) for i in grid]
    print "".join(reversed(g))
if __name__ == '__main__':
  main()
