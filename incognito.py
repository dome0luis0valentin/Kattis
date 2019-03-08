import sys

def main():
  getLine = lambda : sys.stdin.readline().strip()
  n = int(getLine())
  for i in xrange(n):
    m = int(getLine())
    map_ = {}
    for j in xrange(m):
      a,b = getLine().split()
      if b in map_:
        map_[b] += 1
      else:
        map_[b] = 2

    # Think of each catagory as having the option to choose nothing as well
    # If you have n, items - you have n+1 options including the option to
    # to choose nothing. There is one outcome where you choose nothing for
    # every catagory, therefore subtract one
    vals = map_.values()
    vals.append(1) # incase n==0
    total = reduce(lambda x,y: x*y, vals) - 1

    print total

if __name__ == '__main__':
  main()
