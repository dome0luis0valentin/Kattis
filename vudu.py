import sys

def main():
  line = lambda : sys.stdin.readline()
  n = int(line().strip())
  nums = line()
  p = int(line().strip())
  prefix = [0]
  MAX,MIN = 0,0
  for i in nums.split():
    prefix.append(prefix[-1]+(int(i)-p))

  val_map = {}
  MAX = 1
  sorted_vals = sorted(prefix)
  for i in sorted_vals:
    if i not in val_map:
      val_map[i] = MAX
      MAX += 1

  FT = [0 for i in xrange(MAX+1)]
  count = 0
  for i in xrange(n+1):
    val = val_map[prefix[i]]
    index = val
    while index > 0:
      count += FT[index]
      index &= (index-1)
    index = val
    while index <= MAX:
      FT[index] += 1
      index += (index & ~(index-1))
  print count

if __name__ == '__main__':
  main()
