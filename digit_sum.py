import sys

def digit_sum(n):
  if n<=0:
    return 0

  last,remain = n%10, n/10
  if last == 9:
    return digit_sum(remain)*10 + (remain+1)*45
  else:
    s = 0
    r = remain
    while(r != 0):
      s += r%10
      r /=10
    partial =  (last+1)*s + ((last*last +last)/2)
    remain -=1
    return digit_sum(remain)*10 + (remain+1)*45 + partial

def main():
  n = int(sys.stdin.readline().strip())
  for line in sys.stdin:
    a,b = [int(i) for i in line.split()]
    s = 0
    r = a
    while(r!=0):
      s += r%10
      r /= 10
    print digit_sum(b) - digit_sum(a) + s

if __name__ == '__main__':
  main()
