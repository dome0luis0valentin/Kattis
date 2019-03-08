import sys

def rm_tail(s):
  clean = []
  k = len(s)
  for c in reversed(s):
    if c != " ":
      break
    k -= 1
  return s[:k]

def main():
  line = lambda : sys.stdin.readline()[:-1]
  n = int(line())
  all_rots = []
  while n>0:
    fig = []
    max_w = 0
    for i in xrange(n):
      r = list(line())
      if max_w < len(r):
        max_w = len(r)
      fig.append(r)
    rot = [[] for i in xrange(max_w)]
    for i in xrange(n):
      fig[i] += [" "]*(max_w - len(fig[i]))
      for k,c in enumerate(fig[i]):
        if c == "-":
          c = "|"
        elif c == "|":
          c = "-"
        rot[k].append(c)
    rotated = "\n".join(map(lambda x: rm_tail("".join(reversed(x))), rot))
    all_rots.append(rotated)
    n = int(line())
  print "\n\n".join(all_rots)

if __name__ == '__main__':
  main()
