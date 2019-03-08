import sys

def main():
  n = int(sys.stdin.readline().strip())-1
  q = map(int, sys.stdin.readline().split())
  need,i = 1,0
  reqs = []
  while need != 0 and i < n:
    reqs.append(need)
    need = 2*need
    if need <= q[i]: # have enough
      need = 0
      break
    need -= q[i]
    i +=1
  if need > 0:
    print "impossible"
    return

  evens, odds = [],[]
  for i,r in enumerate(reqs):
    if i%2 == 0:
      evens.append(r)
    else:
      odds.append(r)

  a,b = 2**(-1.0*3/4.0), 2**(-1.0*5/4.0)
  ne, de = 0, 2**(len(evens) - 1)
  k = de
  for i in evens:
    ne += k*i
    k/=2

  no, do = 0, 2**(len(odds) - 1)
  k = do
  for i in odds:
    no += k*i
    k/=2
  print (ne*a)/(de*1.0) + (no*b)/(do*1.0)

if __name__ == '__main__':
  main()
