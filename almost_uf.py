import sys

class DSF:
  def __init__(self,n):
    self.size = [1 for i in xrange(n+1)]
    self.sum, self.up, self.parent = range(n+1), range(n+1), range(n+1)

  def find(self, x):
    x = self.up[x]
    p = self.parent[x]
    while p!=x:
      self.parent[x] = self.parent[p]
      x = self.parent[x]
      p = self.parent[x]
    return x

  def union(self,x,y):
    x,y = self.find(x), self.find(y)

    if x==y: return

    if self.size[x] < self.size[y]:
      x,y = y,x
    self.parent[y] = x
    self.size[x] += self.size[y]
    self.sum[x] += self.sum[y]

  def move(self,x,y):
    px,py = self.find(x), self.find(y)
    self.up[x] = py
    self.size[px] -= 1
    self.sum[px] -= x
    self.size[py] += 1
    self.sum[py] += x

  def show(self,x):
    px = self.find(x)
    print self.size[px], self.sum[px]


def main():
  line  = sys.stdin.readline().strip()
  while line != "":
    n,m = [int(i) for i in line.split()]
    disjoint_set = DSF(n)
    for cmd in xrange(m):
      line = [int(i) for i in sys.stdin.readline().split()]
      if line[0] == 1:
        disjoint_set.union(line[1],line[2])
      elif line[0] == 2:
        disjoint_set.move(line[1],line[2])
      else:
        disjoint_set.show(line[1])
    line = sys.stdin.readline().strip()

if __name__ == "__main__":
  main()
