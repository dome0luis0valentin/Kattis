import sys,math
import bisect as bi

def pali(n,b):
  reverse_n = 0;
  temp = n
  while( temp > 0):
    reverse_n = reverse_n*b + temp%b
    temp /= b
  return n == reverse_n

def make_pali(n):
    p1,p2 = n,n
    index = 0
    while (n > 0):
      p1 = p1*2 + n%2
      if (index > 0):
        p2 = p2*2 + n%2
      n/=2
      index +=1
    return p1,p2

def main():
  a,b,k = [int(i) for i in sys.stdin.readline().split()]
  if k >= 4:
    if a > 1:
      print 0
      return
  palis_base2 = [0]
  for i in xrange(1,2000):
    p1,p2 = make_pali(i)
    palis_base2.append(p1)
    palis_base2.append(p2)

  palis_base2.sort()
  lb,ub = bi.bisect_left(palis_base2,a), bi.bisect_left(palis_base2,b)
  c = 0
  for n in palis_base2[lb:ub+1]:
    if n < a:
      continue
    if n > b:
      break
    found = True
    for base in xrange(3,k+1):
      if not pali(n,base):
        found = False
        break
    if found:
      c += 1

  print c

if __name__ == "__main__":
  main()
