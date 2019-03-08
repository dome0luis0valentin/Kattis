import sys

def main():
  n = int(sys.stdin.readline().strip())
  A,B = [0 for i in xrange(101)], [0 for i in xrange(101)]
  for line in sys.stdin:
    a,b = [int(i) for i in line.split()]
    A[a] += 1
    B[b] += 1
    a,b = 100, 1
    ca, cb = 0, 0
    curr_ans = 0
    while True:
      while a>0 and  A[a] == 0:
        a -= 1
      while b<101 and B[b] == 0:
        b +=1
      if (a == 0 or b == 101):
        break
      if ca == 0:
        ca = A[a]
      if cb == 0:
        cb = B[b]
      if a+b > curr_ans:
        curr_ans = a+b
      if ca > cb:
        ca -= cb
        cb = 0
        b+=1
      elif cb > ca:
        cb -= ca
        ca = 0
        a-=1
      else:
        a -= 1
        b += 1
        ca,cb = 0,0
    print curr_ans

if __name__ == '__main__':
  main()

