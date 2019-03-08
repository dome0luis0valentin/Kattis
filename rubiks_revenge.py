import sys

class Config:
  def __init__(self, conf):
    self.config = list(conf)

  def __hash__(self):
    return hash(tuple(self.config))

  def __eq__(self,other):
    return self.config == other.config

  def move_row(self,r):
    mv1, mv2 = self.config[:], self.config[:]
    p1 = 4*r
    p2 = p1 + 3
    for i in xrange(3):
      mv1[p1], mv1[p1+1] = mv1[p1+1], mv1[p1]
      mv2[p2], mv2[p2-1] = mv2[p2-1], mv2[p2]
      p1 += 1
      p2 -= 1
    return Config(mv1),Config(mv2)

  def move_col(self,c):
    mv1, mv2 = self.config[:], self.config[:]
    p1 = c
    p2 = p1 + 12
    for i in xrange(3):
      mv1[p1], mv1[p1+4] = mv1[p1+4], mv1[p1]
      mv2[p2], mv2[p2-4] = mv2[p2-4], mv2[p2]
      p1 += 4
      p2 -= 4
    return Config(mv1), Config(mv2)

  def add_moves(self,moves):
    for i in xrange(4):
      h1,h2 = self.move_row(i)
      v1,v2 = self.move_col(i)
      moves.add(h1)
      moves.add(h2)
      moves.add(v1)
      moves.add(v2)

  def __repr__(self):
    return ",".join([str(i) for i in self.config])

  def __str__(self):
    return self.__repr__()

def bi_dir_BFS(start,target):
  forward_state, back_state = set([start]),set([target])
  next_forward, prev_back = set(), set()
  moves = 0
  while True:
    for i in forward_state:
      if i in back_state:
        return moves
      i.add_moves(next_forward)
    moves += 1
    for i in back_state:
      if i in next_forward:
        return moves
      i.add_moves(prev_back)
    moves +=1
    forward_state , back_state = next_forward,prev_back
    next_forward,prev_back = set(),set()

def main():
  start = []
  for line in sys.stdin:
    start.append(line.strip())
  start = Config("".join(start))
  target = Config("RRRRGGGGBBBBYYYY")
  print bi_dir_BFS(start,target)

if __name__ == '__main__':
  main()
