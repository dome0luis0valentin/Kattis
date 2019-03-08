import sys

def main():
  ascii_nums = [
  '''xxxxx
     x...x
     x...x
     x...x
     x...x
     x...x
     xxxxx''',
  '''....x
     ....x
     ....x
     ....x
     ....x
     ....x
     ....x''',
  '''xxxxx
     ....x
     ....x
     xxxxx
     x....
     x....
     xxxxx''',
  '''xxxxx
     ....x
     ....x
     xxxxx
     ....x
     ....x
     xxxxx''',
  '''x...x
     x...x
     x...x
     xxxxx
     ....x
     ....x
     ....x''',
  '''xxxxx
     x....
     x....
     xxxxx
     ....x
     ....x
     xxxxx''',
  '''xxxxx
     x....
     x....
     xxxxx
     x...x
     x...x
     xxxxx''',
  '''xxxxx
     ....x
     ....x
     ....x
     ....x
     ....x
     ....x''',
  '''xxxxx
     x...x
     x...x
     xxxxx
     x...x
     x...x
     xxxxx''',
  '''xxxxx
     x...x
     x...x
     xxxxx
     ....x
     ....x
     xxxxx''']

  asciis = [ map(lambda x: x.strip(), fig.split("\n")) for fig  in ascii_nums]

  rev_map = dict([ ("".join(fig), str(i)) for i,fig in enumerate(asciis)])
  rows = []
  for line in sys.stdin:
    rows.append(line.strip())

  nums = []
  while len(rows[0]) > 0 :
    fig = []
    for i in xrange(7):
      fig.append(rows[i][:5])
      rows[i] = rows[i][6:]
    nums.append(fig)

  nums = map(lambda x: "".join(x), nums)
  a,b = "",""
  switch = False
  for n in nums:
    if n not in rev_map:
      switch = True
      continue
    if switch:
      b += rev_map[n]
    else:
      a += rev_map[n]
  a,b = int(a), int(b)
  res = str(a+b)
  res_str = [[] for i in xrange(7)]
  for ch in res:
    i = int(ch)
    for k in xrange(7):
      res_str[k].append(asciis[i][k])
  print "\n".join(map(lambda x: ".".join(x),res_str))

if __name__ == '__main__':
  main()
