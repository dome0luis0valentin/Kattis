import sys
from itertools import combinations

def main():
  n,m = [int(i) for i in sys.stdin.readline().split()]
  letters = list("abcdefghijklmnopqrstuvwxyz")
  words = []
  count = 0
  limit = m/2
  for i in combinations(letters,5):
    words.append("".join(i))
    count += 1
    if count > limit:
      break
  if n < count:
    essay = " ".join(words[:min(count,m)])
  else:
    essay_w = words[:n%count]
    reps = " ".join(words)
    for i in xrange(n/count):
      essay_w.append(reps)
    essay = " ".join(essay_w)
  print essay

if __name__ == '__main__':
  main()

