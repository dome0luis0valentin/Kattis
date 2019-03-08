import sys

FLIPS = ('110100000 111010000 011001000 100110100 010111010 001011001 000100110 '+
        '000010111 000001011').split()
FLIPS = map(lambda x: int(x,2), FLIPS)

def bfs(target):
  curr = set([0])
  steps = 0
  seen = set()
  while (target not in curr):
    next_set = set()
    while(len(curr) > 0):
      s = curr.pop()
      if s not in seen:
        for i in FLIPS:
          next_set.add(s^i)
        seen.add(s)
    steps += 1
    curr = curr.union(next_set)
  return steps

def main():
  c = int(sys.stdin.readline().strip())
  for i in xrange(c):
    target = "".join([sys.stdin.readline().strip() for i in range(3)])
    target = int("".join(map(lambda x: '0' if x=='.' else '1', target)),2)
    print bfs(target)

if __name__ == '__main__':
  main()
