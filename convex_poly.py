import sys

def polygonArea(X,Y):
  n = len(X)
  area = 0.0
  j = n-1 # prev
  for i in range(n):
    area += (X[j] + X[i]) * (Y[j] - Y[i])
    j = i
  return abs(area)/2.0

def main():
  sys.stdin.readline()
  for line in sys.stdin:
    X, Y = [], []
    points = line.split()
    for i,p in enumerate(points[1:]):
      if i%2 == 1:
        X.append(int(p))
      else:
        Y.append(int(p))
    print polygonArea(X,Y)

if __name__ == '__main__':
  main()

