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
  n = int(sys.stdin.readline().strip())
  a = [int(i) for i in sys.stdin.readline().split()]
  coeff = [a[0]] + a[-1:0:-1]
  x = [1] + [int(i) for i in sys.stdin.readline().split()]
  xT = [[k] for k in x]

  # Make matrix
  matrix = [ [1] + [0]*n ]
  for i in xrange(1,n):
    row = [0]*(i+1)
    row.append(1)
    matrix.append(row + [0]*(n-i-1))
  matrix.append(coeff)

  # Now handle queries
  queries = int(sys.stdin.readline().strip())
  for j in xrange(queries):
    q,m = [int(k) for k in sys.stdin.readline().split()]
    new_m = matrix_expo(matrix,q,m)
    new_coeff = mult(new_m, xT, m)
    print new_coeff[1][0]

if __name__ == '__main__':
  main()
