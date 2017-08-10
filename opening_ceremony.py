import sys

def main():
    n = int(sys.stdin.readline().strip())
    heights = sorted([int(i) for i in sys.stdin.readline().split()])

    min_charges = n
    for i in range(n):
        h = heights[i]
        curr_charges = h + (n - (i+1))
        if curr_charges < min_charges:
            min_charges = curr_charges
    print min_charges

if __name__ == '__main__':
    main()
