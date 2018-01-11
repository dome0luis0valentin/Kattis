import sys
from heapq import heappush as push,heappop as pop

def simplify(a):
    letter_map = {}
    for i in a:
        if i in letter_map:
            letter_map[i] += 1
        else:
            letter_map[i] = 1
    if len(letter_map)<=2:
        return 0

    ch_list = []
    for k in letter_map:
        ch_list.append((letter_map[k],k))
    ch_list.sort()

    return len(a) - ch_list[-1][0] - ch_list[-2][0]

def main():
    print simplify(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()
