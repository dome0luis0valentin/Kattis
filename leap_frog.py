import sys
from collections import defaultdict
from itertools import product

def chinese_rem(a,n,b,m):
  s, s_prev = 0,1
  t, t_prev = 1,0
  r, r_prev = n,m

  while r != 0:
    q,rem = divmod(r_prev,r)
    r, r_prev = rem, r
    s, s_prev = s_prev - q*s, s

  t = (r_prev - s_prev*n) / m

  g = r_prev
  c1,c2 = s_prev,t
  p = (a-b)/g
  k = (n*m)/g
  x = (b + m*p*c1) % k
  return (x,k)

def multiple_chinese_rem(pairs):
  if len(pairs) == 1:
    return pairs[0]
  n = len(pairs)
  if n%2 == 0:
    first_h, second_h = pairs[:n/2], pairs[n/2:]
    a,n = multiple_chinese_rem(first_h)
    b,m = multiple_chinese_rem(second_h)
  else:
    a,n = pairs[0]
    b,m = multiple_chinese_rem(pairs[1:])
  return chinese_rem(a,n,b,m)

def main():
  line = lambda : sys.stdin.readline().strip()
  t = int(line())
  residues = defaultdict(list)
  for i in xrange(t):
    k,p = map(int, line().split())
    residues[p].append(k)

  possible = []
  height = 0
  for p in residues:
    v = residues[p]
    mini_map = defaultdict(list)
    for i in v:
      mini_map[i%p].append(i)
    poss = []
    max_p = max(map(len, mini_map.values()))
    height += max_p
    for i in mini_map:
      if len(mini_map[i]) == max_p:
        poss.append(map(lambda x:(x,p), mini_map[i]))
    possible.append(poss)

  min_pos = -1
  for k in product(*possible):
    flattened = map(max, k)
    min_p = max(flattened)[0]
    r, mod = multiple_chinese_rem(flattened)
    if r < min_p:
      r = mod*(min_p/mod) + r
      if r < min_p:
        r += mod
    if min_pos == -1 or min_pos > r:
      min_pos = r
  print min_pos, height


if __name__ == '__main__':
  main()
