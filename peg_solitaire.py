import sys

forbidden = set([0,1,2,6,7,8,36,37,38,42,43,44])

def add_moves(peg, conf, add_to):
  conf_p = conf - set([peg])
  r,c = divmod(peg,9)
  for dx,dy in [(0,1), (0,-1), (-1,0), (1,0)]:
    rp, cp = r+dx, c+dy
    if dx == 0 and dy == 1: # jump left
      nxt = rp*9 + cp
      if cp < 8 and nxt in conf:
        nxt_nxt = nxt+1
        if nxt_nxt not in conf and nxt_nxt not in forbidden:
          add_to.append( (conf_p - set([nxt])) | set([nxt_nxt]))
    elif dx == 0 and dy == -1: # jump right
      nxt = rp*9 + cp
      if cp > 0 and nxt in conf:
        nxt_nxt = nxt-1
        if nxt_nxt not in conf and nxt_nxt not in forbidden:
          add_to.append( (conf_p - set([nxt])) | set([nxt_nxt]))
    elif dx == 1 and dy == 0: # jump down
      nxt = rp*9 + cp
      if rp < 4 and nxt in conf:
        nxt_nxt = nxt+9
        if nxt_nxt not in conf and nxt_nxt not in forbidden:
          add_to.append( (conf_p - set([nxt])) | set([nxt_nxt]))
    elif dx == -1 and dy == 0: # jump up
      nxt = rp*9 + cp
      if rp > 0 and nxt in conf:
        nxt_nxt = nxt-9
        if nxt_nxt not in conf and nxt_nxt not in forbidden:
          add_to.append( (conf_p - set([nxt])) | set([nxt_nxt]))

def solve(conf):
  steps = 0
  max_peg = len(conf)
  curr, nxt = [conf], []
  while len(curr)+len(nxt) > 0:
   if len(curr) == 0:
     curr, nxt = nxt, curr
     steps += 1
   q = curr.pop()
   for peg in q:
     add_moves(peg, q, nxt)
  print max_peg-steps, steps



def main():
  n = sys.stdin.readline()
  conf = set()
  row = 0
  for line in sys.stdin:
    if row == 5:
      row = 0
      solve(conf)
      conf = set()
      continue
    line = line.strip()
    for c in xrange(9):
      if line[c] == 'o':
        conf.add(c + row*9)
    row += 1
  solve(conf)

if __name__ == '__main__':
  main()
