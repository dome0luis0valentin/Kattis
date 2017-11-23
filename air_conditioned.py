import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp_ranges = []
    for i in xrange(n):
        t_range = tuple([int(i) for i in sys.stdin.readline().split()])
        temp_ranges.append(t_range)
    temp_ranges = sorted(temp_ranges, key = lambda elem:elem[1])

    rooms = set([])
    count = 0

    for i in temp_ranges:
        flag = True
        for t in xrange(i[0],i[1]+1):
            if t in rooms:
                flag = False
                break
        if flag:
            count += 1
            rooms.add(i[1])
    print count

if __name__ == '__main__':
    main()
