import sys
import math

def main():
    initial = 194 # coresponds 2^1 bit (even tho it doesnt exist)
    for line in sys.stdin:
        year = int(line.strip())/10 # first 3 digits
        if (year == 0):
            return
        diff = year - initial
        max_bits = 2**diff # bits corresponding to current year
        bits = 0.0
        num = 0
        # log of n! is log(1*2*3...*n) = log(1)+log(2)+...+log(n)
        while(max_bits > bits):
            num +=1
            bits += math.log(num,2) # base 2 log - counting digits

        print num - 1

if __name__ == '__main__':
    main()
