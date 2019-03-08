import sys

def main():
  expr = list(sys.stdin.readline().strip())
  pos, stack = [], []
  for i,c in enumerate(expr):
    if c == "(":
      stack.append(i)
    elif c == ")":
      s = stack.pop()
      pos.append((s,i))

  exprs = set()
  for choice in xrange(1, 1<<len(pos)):
    forbidden = set()
    for c in xrange(len(pos)):
      if (choice & 1<<c):
        s,e = pos[c]
        forbidden.add(s)
        forbidden.add(e)
    exprs.add("".join([ch for p,ch in enumerate(expr) if p not in forbidden]))

  for e in sorted(exprs):
    print e

if __name__ == '__main__':
  main()

