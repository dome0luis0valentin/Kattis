import sys
import math

def main():
    f = open(sys.argv[1],"r")
    f.readline()
    for line in f:
        n,m = [int(i) for i in line.split()]
        m = m-1
        ans = math.factorial(n)/(math.factorial(m)*math.factorial(n-m))
        print ans
main()
