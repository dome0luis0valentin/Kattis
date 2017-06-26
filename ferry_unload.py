import sys

LEFT = "left"
RIGHT = "right"

def trips(left,right):
    if len(left)==len(right):
        if right[-1]==0:
            return int(left[-1]!=0)
        else:
            return 2*len(left)
    else:
        return 2*(max(len(left),len(right))) - int(len(right)<len(left))

def main():
    cases = int(sys.stdin.readline().strip())
    for i in range(cases):
        ferry_length, total_cars = map(int, sys.stdin.readline().split())
        ferry_length *= 100 # all units are in cm
        length_l = [0]
        length_r = [0]
        for car in range(total_cars):
            size, side = sys.stdin.readline().split()
            size = int(size)
            if side == LEFT:
                if (length_l[-1]+size < ferry_length):
                    length_l[-1] += size
                else:
                    length_l.append(size)
            else:
                if (length_r[-1]+size < ferry_length):
                    length_r[-1] += size
                else:
                    length_r.append(size)
        print trips(length_l,length_r)

main()
