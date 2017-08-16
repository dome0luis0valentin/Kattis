import sys

def main():
    while True:
        n,m = [int(i) for i in sys.stdin.readline().split()]
        set1 = set()
        if n==0 and m==0:
            break
        for i in xrange(n):
            set1.add(int(sys.stdin.readline().strip()))

        count = 0
        for j in xrange(m):
            count += int(sys.stdin.readline().strip()) in set1
        print count

if __name__ == '__main__':
    main()
