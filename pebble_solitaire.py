import sys

def add_moves(p, conf, q, seen):
  conf_p = conf - frozenset([p])
  # move right
  m = p+1
  mm = p+2
  if mm < 23 and m in conf_p and mm not in conf_p:
    new_c = (conf_p - frozenset([m])) | frozenset([mm])
    if new_c not in seen:
      q.append(new_c)
  # move left
  m = p-1
  mm = p-2
  if mm >= 0 and m in conf_p and mm not in conf_p:
    new_c = (conf_p - frozenset([m])) | frozenset([mm])
    if new_c not in seen:
      q.append(new_c)

def solve(conf):
  min_len = len(conf)
  q = [conf]
  seen = set()
  while len(q) > 0:
    conf = q.pop()
    if conf in seen:
      continue
    else:
      seen.add(conf)
    if len(conf) < min_len:
      min_len = len(conf)
    for p in conf:
      add_moves(p, conf, q, seen)
  return min_len

def main():
  n = sys.stdin.readline()
  for line in sys.stdin:
    conf = []
    for i,c in enumerate(line):
      if c == 'o':
        conf.append(i)
    print solve(frozenset(conf))

if __name__ == '__main__':
  main()
