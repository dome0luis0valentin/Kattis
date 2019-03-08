import sys

def solve(col):
  i = 0
  new_col = []
  apples, spaces = [], []
  while i < len(col):
    if col[i] == ".":
      spaces.append(".")
    elif col[i] == "a":
      apples.append("a")
    else:
      new_col.append("".join(spaces))
      new_col.append("".join(apples))
      new_col.append("#")
      apples, spaces = [], []
    i += 1
  new_col.append("".join(spaces))
  new_col.append("".join(apples))
  return "".join(new_col)

def main():
  line = lambda : sys.stdin.readline()
  r,c = map(int, line().split())
  cols = [[] for i in xrange(c)]
  for line in sys.stdin:
    for i,c in enumerate(line.strip()):
      cols[i].append(c)
  new_cols = []
  for col in cols:
    new_cols.append(solve(col))

  index = 0
  while index < r:
    row = []
    for nc in new_cols:
      row.append(nc[index])
    print "".join(row)
    index += 1


if __name__ == '__main__':
  main()
