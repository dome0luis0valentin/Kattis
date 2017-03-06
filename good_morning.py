import sys
import math

def is_valid(num):
    num = str(num)
    prev_x = -1
    prev_y = -1
    for i in num:
        if i!='0':
            x = int(math.ceil(int(i)/3.0) - 1)
            y = ((int(i) % 3) - 1)%3
        else:
            x = 3
            y = 1
        if prev_x <= x and prev_y<=y:
                prev_x = x
                prev_y = y
        else:
            return False
    return True

def main():
    sys.stdin.readline()
    for line in sys.stdin:
        num = int(line.strip())
        original = num
        alternate = 1
        add = 1
        while not is_valid(num):
            num = original + alternate*(add)
            if alternate == -1:
                add += 1
            alternate *= -1
        print num
main()
