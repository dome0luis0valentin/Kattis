import sys

def max_match(front, back):
  n, m = len(front), len(back)
  for i,ch in enumerate(front[-m:]):
    if front[i] == back[0]:
      poss = front[i:]
      if poss == back[:len(poss)]:
        return len(poss)
  return 0

def main():
  line = lambda : sys.stdin.readline().strip()
  t = int(line())
  for i in xrange(t):
    k,w = [int(k) for k in line().split()]
    count = 0
    prev = ""
    for k in xrange(w):
      curr = line()
      curr_match = max_match(prev, curr)
      count += (len(curr) - curr_match)
      prev = curr
    print count

if __name__ == '__main__':
  main()
