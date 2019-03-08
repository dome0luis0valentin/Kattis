import sys

def odd_binomials(bits):
  if len(bits) == 0:
    return 1

  length = len(bits)-1
  curr = bits.pop()
  if curr == "0":
    return odd_binomials(bits)
  else:
    return (3**length) + (2*odd_binomials(bits))


def main():
  n = int(sys.stdin.readline().strip())-1
  bits = list(reversed(bin(n)[2:]))
  print odd_binomials(bits)

if __name__ == '__main__':
  main()
