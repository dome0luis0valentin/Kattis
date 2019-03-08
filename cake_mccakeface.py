import sys
from collections import defaultdict

def main():
  l = lambda : map(int, sys.stdin.readline().split())
  n = l()[0]
  m = l()[0]
  starts = l()
  ends = l()
  freq = defaultdict(int)
  best_diff, best_freq = 0,0
  for s in starts:
    for e in ends:
      if e >= s:
        c = e - s
        freq[c] += 1
        if freq[c] > best_freq:
          best_diff, best_freq = c, freq[c]
        elif freq[c] == best_freq and best_diff > c:
          best_diff, best_freq = c, freq[c]
  print best_diff

if __name__ == '__main__':
  main()
