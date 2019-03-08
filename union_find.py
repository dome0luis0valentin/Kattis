import sys

class DSF:
  def __init__(self,n):
    self.rank = [0 for i in xrange(n)]
    self.parent = [i for i in xrange(n)]

  def find(self, x):
    p = self.parent[x]
    while p!=x:
      self.parent[x] = self.parent[p]
      x = self.parent[x]
      p = self.parent[x]
    return x

  def union(self,x,y):
    x,y = self.find(x), self.find(y)

    if x==y: return

    if self.rank[x] < self.rank[y]:
      x,y = y,x
    self.parent[y] = x
    if self.rank[x] == self.rank[y]:
      self.rank[x] +=1

def main():
  n,q = [int(i) for i in sys.stdin.readline().split()]
  disjoint_set = DSF(n)
  for line in sys.stdin:
    op,x,y = line.split()
    if op == "=":
      disjoint_set.union(int(x),int(y))
    else:
      if disjoint_set.find(int(x)) == disjoint_set.find(int(y)):
        print "yes"
      else:
        print "no"

if __name__ == "__main__":
  main()
