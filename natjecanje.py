import sys

def main():
  num,s,r = [int(i) for i in sys.stdin.readline().split()]
  n = [1 for i in xrange(num)]
  # Damaged
  for i in sys.stdin.readline().split():
    n[int(i)-1] -= 1
  # Reserved
  for i in sys.stdin.readline().split():
    n[int(i)-1] += 1

  if n[0] == 0 and n[1] == 2:
    n[0] += 1
    n[1] -= 1

  for i in xrange(1,len(n) - 1):
    if n[i] == 0:
      if n[i-1] == 2:
        n[i] +=1
        n[i-1] -=1
      elif n[i+1] == 2:
        n[i] +=1
        n[i+1] -=1
  if n[-1] == 0 and n[-2] == 2:
    n[-1] +=1
    n[-2] -= 1
  cant_start = sum([1 if k == 0 else 0 for k in n])
  print cant_start

if __name__ == '__main__':
  main()
