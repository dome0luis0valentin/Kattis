import sys

def main():
  n = int(sys.stdin.readline().strip())
  data = {}

  for i in xrange(n):
    s,y = sys.stdin.readline().split()
    if s in data:
      data[s][1].append(int(y))
    else:
      data[s] = [False,[int(y)]]

  q = int(sys.stdin.readline().strip())
  for i in xrange(q):
    s,k = sys.stdin.readline().split()
    if not data[s][0]:
      data[s][1].sort()
      data[s][0] = True
    print data[s][1][int(k)-1]

if __name__ == '__main__':
  main()
