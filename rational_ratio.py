import sys
from fractions import gcd

def main():
  n,rep = sys.stdin.readline().split()
  whole, deci = n.split(".")
  rep = int(rep)
  non_rep = len(deci) - rep

  numerator = int(whole+deci) - int(whole+deci[:non_rep])
  denom = 10**len(deci) - 10**non_rep
  com_fact = gcd(numerator,denom)
  print "{0}/{1}".format(numerator/com_fact, denom/com_fact)

if __name__ == '__main__':
  main()
