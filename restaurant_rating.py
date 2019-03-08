import sys

def main():
  # Look up table for # ways to expr "s", as sum of "n" non-negative ints
  table = [[0 for i in xrange(31)], [1 for i in xrange(31)]]
  for n in xrange(2,16):
    curr = []
    for s in xrange(31):
      # computing f(n,s)
      t = 0
      for sp in xrange(s+1):
        t += table[n-1][sp]
      curr.append(t)
    table.append(curr)

  line = sys.stdin.readline().strip()
  while line!= "0":
    nums = [int(i) for i in line.split()]
    n = nums[0]
    scores = nums[1:]
    ss = sum(scores)
    less_or_eq = 1
    # case 1: less total score
    for sp in xrange(ss):
      less_or_eq += table[n][sp]
    # case 2: same sum but lower score from influential critic
    sum_upto = 0
    for p in xrange(1,n):
      # same score, pth critics favore my restaurant
      sum_upto += scores[p-1]
      for k in xrange(1,scores[p-1]+1):
        less_or_eq += table[n-p][ss-sum_upto+k]
    print less_or_eq
    line = sys.stdin.readline().strip()

if __name__ == '__main__':
  main()
