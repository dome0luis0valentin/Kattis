import sys
def main():

    line = sys.stdin.readline().split()
    length = int(line[0])
    d = int(line[1])
    n = int(line[2])
    position = []
    start_flag = True
    end_flag = True
    for line in range(n):
        num = int(sys.stdin.readline().strip())
        position.append(num)
        if (num == 6):
            start_flag = False
        if (num == length -6):
            end_flag = False

    if start_flag:
        position.append(6)         # first possible position
    if end_flag:
        position.append(length-6)  # last possible position
    position.sort()

    total = 0
    for i in range(len(position)-1):
        pos = range(position[i+1],position[i],-d)
        # print pos
        if (pos[-1] - position[i] < d):
            total += len(pos)-1
        else:
            total += len(pos)

    print total + 1 - n

if __name__ == '__main__':
    main()
