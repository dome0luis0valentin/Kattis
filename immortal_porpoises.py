import sys

def mult(A, B, M):
  rows_A = len(A)
  cols_A = len(A[0])
  rows_B = len(B)
  cols_B = len(B[0])

  if cols_A != rows_B:
    return

  # Create the result matrix
  # Dimensions would be rows_A x cols_B
  C = [[0 for row in range(cols_B)] for col in range(rows_A)]

  for i in range(rows_A):
    for k in range(cols_A):
      if A[i][k] != 0:
        for j in range(cols_B):
          C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % M
  return C


def matrix_expo(a,n,m):
  if n == 1:
    return a
  if n%2 == 0:
    half_way = matrix_expo(a , n/2, m)
    return mult(half_way, half_way, m)
  return mult(a, matrix_expo(a, n-1, m),m)

def main():
  fib_matrix = [[0,1],[1,1]]
  line = lambda : sys.stdin.readline().strip()
  t = int(line())
  for i in xrange(t):
    c,n = [int(i) for i in line().split()]
    fn = mult(matrix_expo(fib_matrix,n,10**9), [[0],[1]], 10**9)[0][0]
    print "{} {}".format(c, fn)


if __name__ == '__main__':
  main()
