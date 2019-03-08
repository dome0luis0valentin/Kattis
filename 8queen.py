import sys

def main():
  rows,cols,rd,ld = set(),set(),set(),set()
  y = 0
  queen_count = 0
  flag = False
  for line in sys.stdin:
    for x in xrange(8):
      if line[x] == '*':
        if (y in rows) or (x in cols) or ((x-y) in rd) or ((x+y) in ld):
          flag = True
          break
        rows.add(y)
        cols.add(x)
        rd.add(x-y)
        ld.add(x+y)
        queen_count += 1
    y += 1
    if (flag):
      break
  if (not flag and queen_count == 8):
    print "valid"
  else:
    print "invalid"

if __name__ == '__main__':
  main()

