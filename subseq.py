import sys

def main():
    #sys.stdin = open(sys.argv[1],"r")
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        sys.stdin.readline()
        last = 0
        length = int(sys.stdin.readline().strip())
        array = [int(k) for k in sys.stdin.readline().split()]
        count_map = {0:1}
        count = 0
        for val in array:
            last = val + last
            if last in count_map:
                count_map[last] +=1
            else:
                count_map[last] = 1

            if (last - 47) in count_map:
                count += count_map[last-47]

        print count


if __name__ == '__main__':
    main()
