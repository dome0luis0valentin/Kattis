import sys

def main():
  getline = lambda : sys.stdin.readline().strip()
  n = int(getline())
  runners = []
  for i in xrange(n):
    name,start,other = getline().split()
    start = int("".join(start.split(".")))
    other = int("".join(other.split(".")))
    runners.append((name,start,other))
  runners.sort(key = lambda x:x[2])

  fastest_3 = runners[0][2] + runners[1][2] + runners[2][2]

  fastest_time = 10000 # both times are at most 20secs
  best_starter = 0
  for i in xrange(n):
    if i<3:
      time = fastest_3 + runners[3][2] - runners[i][2] + runners[i][1]
    else:
      time = fastest_3 + runners[i][1]

    if time < fastest_time:
      best_starter = i
      fastest_time = time

  print str(fastest_time)[:-2]+"." + str(fastest_time)[-2:]
  print runners[best_starter][0]
  if best_starter >= 3:
    for k in xrange(3):
      print runners[k][0]
  else:
    for k in xrange(best_starter):
      print runners[k][0]
    for j in xrange(best_starter+1,4):
      print runners[j][0]

if __name__ == '__main__':
  main()
