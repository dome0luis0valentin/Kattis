import sys

def main():
  line = lambda : sys.stdin.readline().strip()
  n = int(line())
  while n!=0:
    cost_mat = [map(int,line().split()) for i in xrange(n)]
    m = int(line())
    costs = map(lambda x: (min(x), max(x)), cost_mat)
    nxt_cost = []
    for i in xrange(m-1):
      for s in xrange(n): # if step m-2-i ended at s
        min_c, max_c = -1,-1
        for k in xrange(n):
          temp_min = cost_mat[s][k] + costs[k][0]
          temp_max = cost_mat[s][k] + costs[k][1]
          if min_c == -1 or min_c > temp_min:
            min_c = temp_min
          if max_c == -1 or max_c < temp_max:
            max_c = temp_max
        nxt_cost.append((min_c, max_c))
      costs, nxt_cost = nxt_cost, []

    print costs[0][1], costs[0][0]
    n = int(line())

if __name__ == '__main__':
  main()
