import sys

def one_side(destinations,k):
  t = 0
  at = len(destinations)-1
  while at >= 0:
    curr_p, mails = destinations[at]
    t += (mails/k)*(2*curr_p)
    last_batch = mails % k
    if last_batch > 0:
      t += (2*curr_p)
    else:
      at -= 1
      continue
    left = k - last_batch
    i = at - 1
    extra_covered = 1
    while left > 0 and i >= 0:
      p,m = destinations[i]
      if m > left:
        m -= left
        left = 0
      else:
        left -= m
        m = 0
        extra_covered += 1
      destinations[i] = (p,m)
      i -= 1
    at -= extra_covered
  return t


def main():
  getInts = lambda : map(int, sys.stdin.readline().split())
  n,k = getInts()
  pos_dest, neg_dest = [], []
  for i in xrange(n):
    p,m = getInts()
    if p > 0:
      pos_dest.append((p,m))
    else:
      neg_dest.append((-1*p,m))
  pos_dest.sort(key = lambda x:x[0])
  neg_dest.sort(key = lambda x:x[0])
  print one_side(pos_dest, k) + one_side(neg_dest, k)


if __name__ == '__main__':
  main()
