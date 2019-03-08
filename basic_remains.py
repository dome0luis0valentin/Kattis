import sys

def str_base(n,base):
  str_rep = []
  while (n != 0):
    (n, m) = divmod(n, base)
    str_rep.append(str(m))
  return "".join(reversed(str_rep)) if len(str_rep)!=0 else "0"

def main():
  for line in sys.stdin:
    line =  line.strip()
    if line == '0':
      return
    b,p,m = line.split()
    b = int(b)
    p = int(p,b)
    m = int(m,b)
    print str_base(p%m,b)

if __name__ == '__main__':
  main()
