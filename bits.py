import sys

def max_bits(n):
  max_sofar = 0
  for i in xrange(1,len(n)+1):
    k = 0
    for bit in bin(int(n[:i]))[2:]:
      if bit == '1':
        k += 1
    if k > max_sofar:
      max_sofar = k
  print max_sofar

def main():
  getline = lambda : sys.stdin.readline().strip()
  n = int(getline())
  for i in xrange(n):
    max_bits(getline())

if __name__ == '__main__':
  main()
