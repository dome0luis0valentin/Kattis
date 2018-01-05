import sys
from fractions import gcd

def main():
    sys.stdin.readline()
    for line in sys.stdin:
        j1,j2,vol = [int(i) for i in line.split()]
        if (vol % gcd(j1,j2) == 0):
            print "Yes"
        else:
            print "No"

if __name__ == '__main__':
    main()
