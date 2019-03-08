import sys

def main():
  sys.stdin.readline()
  dist = defaultdict(list)
  i = 0
  for line in sys.stdin:
    n = int(line.strip())
    dist[n].append(i)
    i += 1
  pos_keys = [ k for k in dist.keys() if len(dist[k]) > 1 ]

  poss_ans = []
  for x in pos_keys:
    for y in pos_keys:


if __name__ == '__main__':
  main()

