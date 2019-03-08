import sys

def solve(table,m,n):
  max_match = 0
  for i in xrange(m-1):
    s1, s2 = table[i], table[i+1]
    match_len = 0
    for c1,c2 in zip(s1,s2):
      if c1 == c2:
        match_len += 1
      else:
        break
    if match_len > max_match:
      max_match = match_len
  return n-max_match-1

def main():
  n, m = map(int, sys.stdin.readline().split())
  table = [[] for i in xrange(m)]
  for line in sys.stdin:
    for i in xrange(m):
      table[i].append(line[i])
  table = sorted(map(lambda x : "".join(reversed(x)), table))
  print solve(table,m,n)

if __name__ == '__main__':
  main()
