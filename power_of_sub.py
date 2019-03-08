import sys

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

def cycles(req, sub_map):
  mod = []
  seen = set()
  for k in req:
    v = req[k]
    a,n = 0,1
    curr = k
    flag = True
    while sub_map[curr-1] != k: # untill we cycle back
      if curr == v:
        flag = False
      if flag:
        a += 1
      curr = sub_map[curr-1]
      n +=1
    if (a,n) not in seen:
      mod.append((a,n))
      seen.add((a,n))
  return mod

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
  t = int(sys.stdin.readline().strip())
  for i in xrange(t):
    length = int(sys.stdin.readline().strip())
    message = [int(i) for i in sys.stdin.readline().split()]
    cypher = [int(i) for i in sys.stdin.readline().split()]

    sub_map = [int(i) for i in sys.stdin.readline().split()]
    requirments = cycles(dict(zip(message,cypher)), sub_map)
    x,k = multiple_chinese_rem(requirments)
    print x

if __name__ == '__main__':
  main()
