import sys

def main():
  q,m,s,l = [int(i) for i in sys.stdin.readline().split()]

  # first run all the Q-second jobs, the run all the 1-Sec jobs
  t = (l/m)*q
  k = m - (l % m)
  if l % m != 0:
    t += q
    if s > k*q:
      s -= k*q
    else:
      s = 0
  t += s/m
  if s%m != 0:
    t += 1
  print t


if __name__ == '__main__':
  main()
