import sys,math

def main():
    n = int(sys.stdin.readline().strip())
    second_half = []
    sqrt_n =  int(math.sqrt(n))
    for i in xrange(1,sqrt_n+1):
        if n%i == 0:
            print i-1,
            second_half.append((n/i)-1)
    start = -1 - (sqrt_n*sqrt_n == n)
    for d in second_half[start:0:-1]:
        print d,
    print second_half[0]
if __name__ == '__main__':
    main()
