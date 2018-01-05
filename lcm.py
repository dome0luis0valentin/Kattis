import sys
from fractions import gcd

def main():
    lcm = lambda a,b : (a/(gcd(a,b)))*b
    for line in sys.stdin:
        a = [int(i) for i in line.split()]
        print reduce(lcm,a)

if __name__ == '__main__':
    main()
