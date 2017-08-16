import sys

def main():
    sys.stdin.readline()

    heights = [int(i) for i in sys.stdin.readline().split()]
    count = 0
    open_arrows = [0 for i in xrange(10**6 + 1)]
    for i in heights:
        if open_arrows[i] > 0:
            open_arrows[i] -= 1
        else:
            count +=1

        open_arrows[i-1] += 1
    print count


if __name__ == '__main__':
    main()
