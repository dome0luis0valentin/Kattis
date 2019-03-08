import sys

def main():
  cases = int(sys.stdin.readline().strip())
  for c in xrange(cases):
    n = int(sys.stdin.readline().strip())
    curr_max,winner = 0,0
    same = 0
    total = 0
    for i in xrange(n):
      v = int(sys.stdin.readline().strip())
      if v > curr_max:
        curr_max = v
        same = 1
        winner = i
      elif v == curr_max:
        same += 1
      total += v
    if same > 1:
      print "no winner"
    elif curr_max*2 > total:
      print "majority winner {}".format(winner+1)
    else:
      print "minority winner {}".format(winner+1)

if __name__ == '__main__':
  main()
