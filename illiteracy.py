import sys

rot = dict(zip("ABCDEF", "BCDEFA"))
def move(p,c, conf):
  conf = list(conf)
  if c == "A":
    v = p-1
    if v >= 1:
      conf[v-1] = rot[conf[v-1]]
    v = p+1
    if v <= 8:
      conf[v-1] = rot[conf[v-1]]
  elif c == "B":
    if p!= 1 and p!= 8:
      v1,v2 = p-1,p+1
      conf[v2-1] = conf[v1-1]
  elif c == "C":
    v = 9-p-1
    conf[v] = rot[conf[v]]
  elif c == "D":
    lb, up = (0,p-1) if p <= 4 else (p,8)
    for k in xrange(lb,up):
      conf[k] = rot[conf[k]]
  elif c == "E":
    diff = min(p-1, 8-p)
    v1, v2 = p-diff-1, p+diff-1
    conf[v1] = rot[conf[v1]]
    conf[v2] = rot[conf[v2]]
  elif c == "F":
    v = (p+9)/2 if p%2 == 1 else p/2
    conf[v-1] = rot[conf[v-1]]
  return "".join(conf)

def path(start, end):
  q = [start]
  seen = set()
  steps = 0
  while len(q) > 0:
    nxt = []
    while len(q) > 0:
      curr = q.pop()
      if curr == end:
        return steps
      #seen.add(curr)
      for i,c in enumerate(curr):
        res = move(i+1,c,curr)
        if res not in seen:
          nxt.append(res)
          seen.add(res)
    steps +=1
    q = nxt

  return -1

def main():
  start = sys.stdin.readline().strip()
  end = sys.stdin.readline().strip()
  print path(start, end)

if __name__ == '__main__':
  main()
