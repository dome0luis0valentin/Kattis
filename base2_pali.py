import sys, bisect as b

def f(n):
  if n<3:
    return 1
  n -=2
  return 2**((n+1)/2)

def make_map(limit = 50000):
  s = [0]
  length = 1
  while s[-1] < limit:
    s.append(s[-1]+f(length))
    length +=1
  return s

def main():
  s = make_map()
  m = int(sys.stdin.readline())
  small = {1:1, 2:3, 3:5,4:7}
  if m <=4:
    print small[m]
    return
  pali_len = b.bisect_left(s,m)
  nth = m - s[pali_len-1] - 1
  bin_rep = bin(nth)[2:]
  if pali_len % 2 == 0:
    bin_rep = bin_rep.rjust((pali_len/2)-1,'0')
    for i in reversed(bin_rep):
      bin_rep += i
  else:
    bin_rep = bin_rep.rjust(pali_len/2,'0')
    for i in reversed(bin_rep[:-1]):
      bin_rep += i

  bin_rep = "1{}1".format(bin_rep)
  print int(bin_rep,2)

if __name__ == '__main__':
  main()
