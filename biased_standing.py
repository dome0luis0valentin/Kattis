import sys
import heapq as H

def main():

    cases = int(sys.stdin.readline().strip())
    sys.stdin.readline()

    for i in range(cases):
        size = int(sys.stdin.readline().strip())
        PQ = []
        for k in range(size):
            val = int(sys.stdin.readline().split()[-1])
            H.heappush(PQ,val)

        badness = 0
        curr_rank = 1
        PQ.sort()
        for rank in PQ:
            badness += abs(rank-curr_rank)
            curr_rank += 1
        print badness
        sys.stdin.readline()


if __name__ == '__main__':
    main()
