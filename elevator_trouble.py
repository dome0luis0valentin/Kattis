import sys

def solve(floors, start, goal, up, down):
  if start == goal:
    return 0
  q_f, q_b = [start], [goal]
  seen_f = [False for i in xrange(floors+1)]
  seen_b = [False for i in xrange(floors+1)]

  steps_f, steps_b = 0,0
  seen_f[start] = True
  seen_b[goal] = True
  while len(q_f) > 0 and len(q_b) > 0:
    # forward
    nxt = []
    while len(q_f) > 0:
      curr = q_f.pop()
      if seen_b[curr]:
        return steps_f + steps_b
      seen_f[curr] = True
      f, b = curr+up, curr-down
      if f <= floors and not seen_f[f]:
        nxt.append(f)
        seen_f[f] = True
      if b > 0 and not seen_f[b]:
        nxt.append(b)
        seen_f[b] = True
    steps_f += 1
    q_f = nxt
    # backward
    nxt = []
    while len(q_b) > 0:
      curr = q_b.pop()
      if seen_f[curr]:
        return steps_f + steps_b
      seen_b[curr] = True
      f, b = curr-up, curr+down
      if 0 < f and not seen_b[f]:
        nxt.append(f)
        seen_b[f] = True
      if b <= floors and not seen_b[b]:
        nxt.append(b)
        seen_b[b] = True
    steps_b += 1
    q_b = nxt

  return "use the stairs"


def main():
  print solve(*map(int,sys.stdin.readline().split()))

if __name__ == '__main__':
  main()
