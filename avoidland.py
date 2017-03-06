import sys
import Queue as Q

def main():
    n = int(sys.stdin.readline().strip())

    rows = Q.PriorityQueue()
    cols = Q.PriorityQueue()

    for line in sys.stdin:
        r,c = [int(k) for k in line.split()]
        rows.put(r)
        cols.put(c)

    steps = 0
    for i in range(1,n):
        steps += abs(rows.get() - i)
        steps += abs(cols.get() - i)
    print steps


if __name__ == '__main__':
    main()
