import sys

def use_onePoint(A,B,C,start,end):
  a,b,c = A[end] - A[start], B[end] - B[start], C[end] - C[start]
  if a == b == c == 0:
    return 0
  x = int(round( b/(2.0*a) ))
  return a*x*x - b*x + c

def posterize(A,B,C, distinct, allowed):
  # if we used only one point for the first i distinct red values
  prev = [use_onePoint(A,B,C,0,i) for i in xrange(distinct+1)]
  curr = [0 for i in xrange(distinct+1)]
  for j in xrange(2,allowed+1): # j is number of posterizing values to use
    for i in xrange(2,distinct+1): # i is number of distinct reds in considerations
      min_sofar = -1
      for k in xrange(1,i+1):
        curr_mse = prev[k] + use_onePoint(A, B, C, k, i)
        if curr_mse < min_sofar or min_sofar == -1:
          min_sofar = curr_mse
      curr[i] = max(0,min_sofar)
    prev, curr = curr[:], [0 for i in xrange(distinct+1)]
  return prev[distinct]

def main():
  line = lambda : sys.stdin.readline().strip()
  k,d = [int(i) for i in line().split()]

  reds = []
  A, B, C = [0], [0], [0]
  for i in xrange(k):
    val,weight = [int(i) for i in line().split()]
    A.append(A[-1] + weight)
    B.append(B[-1] + 2*val*weight)
    C.append(C[-1] + val*val*weight)
    reds.append( [val,weight] )

  print posterize(A, B, C, k, d)

if __name__ == '__main__':
  main()
