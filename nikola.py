import sys

def shortest(fee,n):
  table = [ [-1]*(n+1) for i in xrange(n+1) ] # x=steps, y=sq num
  for step in xrange(n, -1, -1):
    for sq in xrange(1,n+1):
      if sq == n:
        table[step][sq] = fee[-1]
        continue
      sq_f = sq + step + 1
      sq_b = sq - step
      if sq_f <= n and step < n: # forward step is valid
        if table[step+1][sq_f] != -1:
          v = table[step+1][sq_f] + fee[sq-1]
          table[step][sq] = v
      if sq_b > 0: # back move is valid
        if table[step][sq_b] != -1:
          v = table[step][sq_b] + fee[sq-1]
          if table[step][sq] == -1 or v < table[step][sq]:
            table[step][sq] = v
  return table[1][2]

def main():
  n = int(sys.stdin.readline().strip())
  fee = []
  for line in sys.stdin:
    fee.append(int(line.strip()))
  print shortest(fee, n)

if __name__ == '__main__':
  main()
