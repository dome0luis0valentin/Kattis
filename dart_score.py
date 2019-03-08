import sys

possible_score = set(range(1,21)) | set([2*i for i in range(1,21)]) | set([3*i for i in range(1,21)])

def rep(n, tries):
  if tries == 0:
    return []
  if n in possible_score:
    return [n]

  for i in possible_score:
    if i < n:
      rest = rep(n-i, tries-1)
      if len(rest) > 0:
        rest.append(i)
        return rest
  return []

def main():
  v = int(sys.stdin.readline().strip())
  reps = rep(v,3)
  for r in reps:
    if r <= 20:
      print "single {}".format(r)
    elif r % 3 == 0:
      print "triple {}".format(r/3)
    else:
      print "double {}".format(r/2)
  if len(reps) == 0:
    print "impossible"

if __name__ == '__main__':
  main()
