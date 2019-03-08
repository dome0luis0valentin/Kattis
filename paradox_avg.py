import sys, bisect

def main():
  line = lambda : sys.stdin.readline().strip()
  t = int(line())
  for i in xrange(t):
    line()
    n1, n2 = [int(k) for k in line().split()]
    all_nums  = []
    while len(all_nums) != n1+n2:
      nums = [int(k) for k in line().split()]
      all_nums += nums
    cs,e = all_nums[:n1], all_nums[n1:]
    cs_avg = sum(cs)/(n1*1.0)
    if n2 > 0 :
      e_avg  = sum(e) /(n2*1.0)
    else:
      e_avg = 0

    valid = [k for k in cs if k < cs_avg and k>e_avg]
    print len(valid)


if __name__ == '__main__':
  main()
